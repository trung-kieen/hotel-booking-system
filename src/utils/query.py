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
