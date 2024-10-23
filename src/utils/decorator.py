"""
Author: Nguyen Khac Trung Kien
"""


from utils.logging import  app_logger
from typing import final
from components.messagebox.popup import BasePopup, ErrorPopup
from database.orm import Session


def handle_exception(f, business_error_message = "Something went wrong" ):
    """
    Make sure application error will not crash program
    Provide business message to user reader
    """
    def wrapper ( * args  , ** kwargs):
        try:
            return f(*args , ** kwargs)
        except Exception as ex:
            app_logger.error("Error occur %s" , ex)
            ErrorPopup(message=business_error_message)
    return wrapper


def transaction(f):
    """
    Specific session passin or wrapper function will generate for you
    def f1(a, b, c, Session=None, **kwargs)
    def f2(*args, Session=None, **kwargs)
    Session must declare between
    It you not pass session value it still inject session for you. The only disavantage is
    that variable session type is unknow till runtime, so your ide will not regcognize them
    Usage: use session between args and kwargs
    def f3(a, b, session=None, c=10)
    def f4(a, b, session=Session(), c=10)
    """
    def wrapper(* args ,** kwargs):
        session  = kwargs.get("session", Session())
        try:
            f(*args, session = session  ,  **kwargs)
            session.commit()
        except:
            app_logger.error("Transaction failed. Rollback to previous stage")
            session.rollback()
        finally:
            session.close()
    return wrapper
