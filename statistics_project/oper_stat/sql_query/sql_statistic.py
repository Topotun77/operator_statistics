# Общее количество успешных звонков по каждой из баз.
# Здесь выбрано поле campaign, т.к. непонятно, что такое base, но можно заменить
# campaign на base
count_success_call = """
SELECT operator, campaign, COUNT(*) AS successful_calls_count
FROM call
WHERE success = TRUE
GROUP BY operator, campaign;
"""

# Среднее количество успешных звонков в день. Дни, в которые оператор не совершил ни
# одного звонка или количество звонков сильно отклоняется от дневной нормы, учитываться не
# должны. Например, если в среднем оператор делает 100 звонков, но в определенный день
# сделал только 15, звонки в этот день не должны учитываться в рассчитанном значении.
avg_success_call_in_dey = """
WITH daily_calls AS (
    SELECT
        b.received_date AS call_day,
        c.operator AS operator,
        SUM(CASE WHEN c.success THEN 1 ELSE 0 END) AS successful_calls
    FROM call c
    JOIN base b ON c.campaign = b.campaign
    GROUP BY call_day, c.operator
),
average_daily_calls AS (
    SELECT
        operator,
        AVG(successful_calls) AS avg_calls,
        STDDEV_SAMP(successful_calls) AS std_dev
    FROM daily_calls
    GROUP BY operator
),
filtered_days AS (
    SELECT
        dc.call_day,
        dc.operator,
        dc.successful_calls
    FROM daily_calls dc
    JOIN average_daily_calls adc ON dc.operator = adc.operator
    WHERE ABS(dc.successful_calls - adc.avg_calls) <= 2 * adc.std_dev
)
SELECT
    fd.operator,
    CAST(AVG(fd.successful_calls) AS FLOAT) AS filtered_avg_calls
FROM filtered_days fd
GROUP BY fd.operator;
"""

# Средняя дневная конверсия (отношение успешных звонков к общему количеству
# совершенных звонко). Выбросы должны отсеиваться так же, как для предыдущего пункта.
avg_conversion_call_in_dey = """
WITH daily_calls AS (
    SELECT
        b.received_date AS call_day,
        c.operator,
        COUNT(*) AS total_calls,
        SUM(CASE WHEN c.success THEN 1 ELSE 0 END) AS successful_calls
    FROM call c
    JOIN base b ON c.campaign = b.campaign
    GROUP BY call_day, c.operator
),
average_daily_calls AS (
    SELECT
        operator,
        AVG(total_calls) AS avg_calls,
        STDDEV_SAMP(total_calls) AS std_dev
    FROM daily_calls
    GROUP BY operator
),
filtered_days AS (
    SELECT
        dc.call_day,
        dc.operator,
        dc.total_calls,
        dc.successful_calls
    FROM daily_calls dc
    JOIN average_daily_calls adc ON dc.operator = adc.operator
    WHERE ABS(dc.total_calls - adc.avg_calls) <= 2 * adc.std_dev
)
SELECT
    fd.operator,
    AVG((CAST(fd.successful_calls AS FLOAT) / CAST(fd.total_calls AS FLOAT)) * 100) AS avg_conversion_rate
FROM filtered_days fd
GROUP BY fd.operator;
"""

# Средняя длительность успешного разговора (считаются все разговоры)
avg_duration_success = """
SELECT operator, CAST(AVG(COALESCE(duration, 0)) AS FLOAT) AS average_duration
FROM call
WHERE success = TRUE
GROUP BY operator;
"""

# Средняя длительность неуспешного разговора.
avg_duration_not_success = """
SELECT operator, CAST(AVG(duration) AS FLOAT) AS average_duration
FROM call
WHERE success = FALSE
GROUP BY operator;
"""
