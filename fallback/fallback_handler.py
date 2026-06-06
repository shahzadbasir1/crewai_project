class FallbackHandler:

    @staticmethod
    def handle_search_failure(query: str) -> str:

        return (
            f"Fallback Activated\n\n"
            f"Unable to retrieve live search results "
            f"for '{query}'.\n\n"
            f"Proceeding using internal knowledge."
        )

    @staticmethod
    def handle_file_failure(filepath: str) -> str:

        return (
            f"Fallback Activated\n\n"
            f"Unable to read file:\n"
            f"{filepath}"
        )

    @staticmethod
    def handle_llm_failure(error: str) -> str:

        return (
            f"Fallback Activated\n\n"
            f"LLM Error:\n"
            f"{error}"
        )

    @staticmethod
    def handle_empty_response() -> str:

        return (
            "Fallback Activated\n\n"
            "No meaningful response generated."
        )