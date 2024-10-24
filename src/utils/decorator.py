"""
Author: Nguyen Khac Trung Kien
"""


import sqlalchemy
from utils.logging import  app_logger
from typing import final
from database.orm import Session
from components.messagebox.popup import BasePopup, ErrorPopup
from sqlalchemy.orm import sessionmaker, Session as SessionType


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
            # TODO: Use business error message for production
            # ErrorPopup(message=business_error_message)
            ErrorPopup(message=str(ex) )
    return wrapper


def transaction(f, business_error_message = "Something went wrong"):
    """
    Specific session passin or wrapper function will generate for you
    def f1(a, b, c, Session=None, **kwargs)
    def f2(*args, Session=None, **kwargs)
    Session must declare between
    It you not pass session value it still inject session for you. The only disavantage is
    that variable session type is unknow till runtime, so your ide will not regcognize them
    Display error message as messagebox like `handle_exception`
    Usage: use session between args and kwargs
    def f3(a, b, session=None, c=10)
    def f4(a, b, session=Session(), c=10)
    """
    def wrapper(* args ,** kwargs):
        # Inject both args and kwargs
        session : SessionType  = kwargs.get("session", Session())
        try:
            session.begin()
            f(*args, session = session  ,  **kwargs)
            session.commit()
        except sqlalchemy.exc.IntegrityError as ex:

            # TODO: Use context of business_error_message to transalate senmantic error message for user
            ErrorPopup(message="Violate reference constraint! Can not delete this record due to cascade deletion\n" +  str(ex) )
        except sqlalchemy.exc.OperationalError as ex :
            ErrorPopup(message="Optional error occur in database\n" +  str(ex) )
        except Exception as ex:
            app_logger.error("Transaction failed. Rollback to previous stage")
            # ErrorPopup(message=business_error_message)

            ErrorPopup(message=str(ex) )
            session.rollback()
        finally:
            session.close()
    return wrapper
