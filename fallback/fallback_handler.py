from monitoring.langfuse_config import langfuse


class FallbackHandler:

    @staticmethod
    def handle_search_failure(query: str) -> str:

        try:

            langfuse.create_event(
                name="Search Fallback Activated",
                input={
                    "query": query
                }
            )

            langfuse.flush()

        except Exception:
            pass

        return (
            f"Fallback Activated\n\n"
            f"Unable to retrieve live search results "
            f"for '{query}'.\n\n"
            f"Proceeding using internal knowledge."
        )

    @staticmethod
    def handle_file_failure(filepath: str) -> str:

        try:

            langfuse.create_event(
                name="File Fallback Activated",
                input={
                    "filepath": filepath
                }
            )

            langfuse.flush()

        except Exception:
            pass

        return (
            f"Fallback Activated\n\n"
            f"Unable to read file:\n"
            f"{filepath}"
        )

    @staticmethod
    def handle_llm_failure(error: str) -> str:

        try:

            langfuse.create_event(
                name="LLM Fallback Activated",
                input={
                    "error": error
                }
            )

            langfuse.flush()

        except Exception:
            pass

        return (
            f"Fallback Activated\n\n"
            f"LLM Error:\n"
            f"{error}"
        )

    @staticmethod
    def handle_empty_response() -> str:

        try:

            langfuse.create_event(
                name="Empty Response Fallback"
            )

            langfuse.flush()

        except Exception:
            pass

        return (
            "Fallback Activated\n\n"
            "No meaningful response generated."
        )