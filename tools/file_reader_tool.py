from crewai.tools import BaseTool

from fallback.fallback_handler import FallbackHandler

from monitoring.trace_helper import (
    start_trace,
    end_trace
)


class FileReaderTool(BaseTool):
    name: str = "File Reader Tool"
    description: str = (
        "Reads the contents of a text file "
        "and returns the contents."
    )

    def _run(self, filepath: str) -> str:

        trace = start_trace(
            "File Reader Tool",
            {
                "filepath": filepath
            }
        )

        try:

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as f:

                result = f.read()

            end_trace(
                trace,
                result
            )

            return result

        except Exception:

            result = (
                FallbackHandler
                .handle_file_failure(filepath)
            )

            end_trace(
                trace,
                result
            )

            return result