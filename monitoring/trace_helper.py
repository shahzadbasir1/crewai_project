from monitoring.langfuse_config import langfuse


def start_trace(name, input_data):

    observation = langfuse.start_observation(
        name=name,
        input=input_data
    )

    return observation


def end_trace(
    observation,
    output_data
):

    observation.update(
        output=output_data
    )

    langfuse.flush()