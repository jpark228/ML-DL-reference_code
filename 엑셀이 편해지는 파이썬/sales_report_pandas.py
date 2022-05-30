from pathlib import Path

import pandas as pd


# 이 파일의 디렉토리
this_dir = Path(__file__).resolve().parent

# sales_data의 서브디렉토리에 있는 엑셀 파일을 모두 읽습니다
parts = []
for path in (this_dir / "sales_data").rglob("*.xls*"):
    print(f'Reading {path.name}')
    part = pd.read_excel(path, index_col="transaction_id")
    parts.append(part)

# 각 파일의 데이터프레임을 하나로 조합합니다
# 열 정렬은 판다스에 알아서 합니다
df = pd.concat(parts)

# 피벗을 사용해 각 대리점을 열 하나로 모으고 일별 거래량을 합산합니다
pivot = pd.pivot_table(df,
                       index="transaction_date", columns="store",
                       values="amount", aggfunc="sum")

# 월말로 리샘픔링을 적용하고 인덱스 이름을 할당합니다
summary = pivot.resample("M").sum()
summary.index.name = "Month"

# 요약 보고서를 엑셀 파일로 만듭니다
summary.to_excel(this_dir / "sales_report_pandas.xlsx")