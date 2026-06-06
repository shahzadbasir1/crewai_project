from crewai.tools import BaseTool


class FileReaderTool(BaseTool):
    name: str = "File Reader Tool"
    description: str = "Reads a text file"

    def _run(self, filepath: str) -> str:

        try:
            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as f:

                return f.read()

        except Exception as e:
            return str(e)