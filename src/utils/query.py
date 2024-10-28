"""
Author: Nguyen Khac Trung Kien
"""
query_get_room_by_total_capacity  = """
SELECT
  room_id AS 'room id',
  SUM(capacity) as capacity,
  floor_id as 'floor id',
  is_locked as 'is locked',
  price as 'PRICE',
  room_type as 'room type'
FROM
  (
    SELECT
      A.id as room_id,
      room_type,
      floor_id,
      is_locked,
      price,
      bed_type_id,
      name,
      (T.capacity * bed_amount) as capacity
    FROM
      (SELECT * FROM  rooms WHERE {0} LIMIT {1} )  AS A
      INNER JOIN bed_rooms AS B
      INNER JOIN bed_types AS T
    WHERE
      A.id = B.room_id
      AND T.id = B.bed_type_id
  )
GROUP BY
  room_id
"""


query_today_booking_status = """
SELECT status, COUNT(*) FROM
 (SELECT id, customer_id, start_date, checkin, checkout, end_date, num_adults, num_children, room_id, is_canceled, booking_type, created_at,
     CASE
     WHEN is_canceled = True  THEN 'CANCELED'
     WHEN checkin is NULL THEN 'INCOMING'
     --  Checkout is null => Check if overdue or using room in booking time
     WHEN checkout IS NULL and DATETIME('now') < end_date THEN 'IN TIME'
    ELSE
        'OVERDUE'
    END
 AS 'status'

 FROM bookings

-- condition to checkout bound range booking tie with today
-- if overdue room => checkout is null  and now > end_date
-- else we assume  start_date <= now  <= end_date
WHERE (start_date  <= DATETIME('now') and  end_date >= DATETIME('now')) OR checkout IS NULL)
GROUP BY status
"""


DAY_PERIOD  = 'd'
MONTH_PERIOD  = 'm'
QUARTER_PERIOD  = 'q'
YEAR_PERIOD  = 'y'
query_invoice_total_group_by_period = """
SELECT period , SUM(total_price)
FROM (
SELECT
    CASE
        WHEN :period = 'd' THEN strftime('%Y-%m-%d', created_at)  -- Group by day
        WHEN :period = 'm' THEN strftime('%m', created_at)    -- Group by month
        WHEN :period = 'q' THEN
            CASE
                WHEN strftime('%m', created_at) BETWEEN '01' AND '03' THEN 'Q1'
                WHEN strftime('%m', created_at) BETWEEN '04' AND '06' THEN 'Q2'
                WHEN strftime('%m', created_at) BETWEEN '07' AND '09' THEN 'Q3'
                WHEN strftime('%m', created_at) BETWEEN '10' AND '12' THEN 'Q4'
            END
        WHEN :period = 'y' THEN strftime('%Y', created_at)       -- Group by year
    END AS period, total_price  -- or any aggregate function you need

FROM invoices
WHERE
    (:period = 'd' AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')) -- Filter for this month
    OR
    (:period = 'm' AND strftime('%Y', created_at) = strftime('%Y', 'now')) -- Filter for this year
    OR
    (:period = 'q' AND strftime('%Y', created_at) = strftime('%Y', 'now')) -- Filter for this year
    OR
    (:period = 'y')

)
GROUP BY period
ORDER BY period;
"""

query_today_income= """
SELECT COALESCE(SUM(total_price), 0) AS total_income FROM invoices WHERE strftime('%Y-%m-%d', created_at) = strftime('%Y-%m-%d', 'now')
"""


query_this_month_income= """
SELECT COALESCE(SUM(total_price), 0) AS total_income FROM invoices WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
"""
