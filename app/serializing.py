import pandas as pd
import json
import re


def convert_mail_object(data: str) -> pd.DataFrame:
    mail = json.loads(data)
    list_keys = [key for key in mail.keys() if re.match(r'Лист\d+', key)]

    dfs = []
    for key in list_keys:
        df = pd.json_normalize(mail[key])
        dfs.append(df)

    render_data = pd.concat(dfs, ignore_index=True)
    column_name = 'Номер документа, яким затверджено місцеву Програму'
    render_data[column_name] = render_data[column_name].astype(str)

    return render_data
