from tools.search_tool import SerperSearchTool
from tools.file_reader_tool import FileReaderTool
from tools.trend_score_tool import TrendScoreTool

print("\nFILE TOOL")
print("=" * 50)

print(
    FileReaderTool()._run(
        "data/sample_report.txt"
    )
)

print("\nTREND TOOL")
print("=" * 50)

print(
    TrendScoreTool()._run(
        "AI payroll automation"
    )
)

print("\nSEARCH TOOL")
print("=" * 50)

print(
    SerperSearchTool()._run(
        "Latest AI trends"
    )
)