import sys
from fastapi import FastAPI
from typing import List, Tuple
from pydantic import BaseModel
from pandas import DataFrame
from utills.filter import filter_data
import uvicorn
import logging

app = FastAPI()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # 设置日志级别为 INFO

# 创建一个 StreamHandler 并设置日志格式
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# 将 StreamHandler 添加到 logger
logger.addHandler(ch)

@app.post("/filter-data")
async def get_filter_data():  # 修改这里
    print('一切都准备好了就在浏览器或者apipost 向我发送http请求吧')
    logger.info("Function get_filter_data is called.")
    records = [
        {'日期': '2022-01-01', '收入/支出': '收入', '金额': 100, '明细备注': '工资'},
        {'日期': '2022-01-02', '收入/支出': '支出', '金额': -50, '明细备注': '购物'},
        {'日期': '2022-02-01', '收入/支出': '收入', '金额': 200, '明细备注': '奖金'}
    ]

    view = 'monthly'
    selected_date = '2022/01'

    filtered_df, income_total, expense_total = filter_data(records, view, selected_date)
    logger.info("Function get_filter_data completed.")
    return {"filtered_df": filtered_df.to_dict(orient="records"), "income_total": income_total, "expense_total": expense_total}

if __name__ == "__main__":
    uvicorn.run("utills.test_app:app", host="127.0.0.1", port=8000, reload=True)