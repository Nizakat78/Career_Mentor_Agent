import chainlit as cl
from agents import Runner
from Expert.career_agent import career_agent
from set_config import google_gemini_config

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    cl.user_session.set("agent", career_agent)
    await cl.Message(content="Welcome to Career Mentor Agent!").send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": msg.content})

    thinking = cl.Message(content="Thinking ...")
    await thinking.send()

    try:
        agent = cl.user_session.get("agent", career_agent)
        result = await Runner.run(
            agent,
            history,
            run_config=google_gemini_config,
        )

        # ✅ Use final_output instead of output
        output = result.final_output if hasattr(result, "final_output") else "[No output returned]"
        thinking.content = output
        await thinking.update()

        if hasattr(result, "to_input_list"):
            cl.user_session.set("history", result.to_input_list())

    except Exception as e:
        thinking.content = f"Error: {e}"
        await thinking.update()
