CREATE EXTERNAL SCHEMA kinesis_schema
FROM KINESIS
IAM_ROLE default;

CREATE MATERIALIZED VIEW customer_stream AS
SELECT ApproximateArrivalTimestamp,
JSON_PARSE(from_varbyte(Data, 'utf-8')) as customer_data
FROM kinesis_schema.customer_stream
WHERE is_utf8(Data) AND is_valid_json(from_varbyte(Data, 'utf-8'));


CREATE MATERIALIZED VIEW order_stream AS
SELECT ApproximateArrivalTimestamp,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'consignmentid', true) AS BIGINT) as consignmentid,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'timestamp', true) AS VARCHAR(50)) as order_timestamp,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delivery_address', true) AS VARCHAR(100)) as delivery_address,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delivery_state', true) AS VARCHAR(50)) as delivery_state,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'origin_address', true) AS VARCHAR(100)) as origin_address,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'origin_state', true) AS VARCHAR(50)) as origin_state,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delay_probability', true) AS VARCHAR(10)) as delay_probability,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'days_to_deliver', true) AS INT) as days_to_deliver,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'delivery_distance', true) AS FLOAT) as delivery_distance,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'userid', true) AS INT) as userid,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'revenue', true) AS FLOAT) as revenue,
CAST(JSON_EXTRACT_PATH_TEXT(from_varbyte(Data, 'utf-8'), 'cost', true) AS FLOAT) as cost
FROM kinesis_schema.order_stream
WHERE is_utf8(Data) AND is_valid_json(from_varbyte(Data, 'utf-8'));