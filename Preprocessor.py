import re
import pandas as pd


def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_name': messages, 'date': dates})

    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y, %H:%M - ')

    user = []
    message = []

    for messages in df['user_name']:
        entry = re.split('([\w\W]+?):\s', messages)
        if entry[1:]:  # user name
            user.append(entry[1])
            message.append(entry[2])
        else:
            user.append('group_notification')
            message.append(entry[0])

    df['user'] = user
    df['message'] = message
    df.drop(columns=['user_name'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['exact_date'] = df['date'].dt.date

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + '-' + str('00'))
        elif hour == 0:
            period.append(str('00') + '-' + str(hour + 1))
        else:
            period.append(str(hour) + '-' + str(hour + 1))

    df['period'] = period


    return df