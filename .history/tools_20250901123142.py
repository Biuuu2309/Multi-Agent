def ResearchPlanner(session):
    session.state.subtasks = create_subtasks(session.input)

def DataGatherer(session):
    subtasks = session.state.subtasks
    results = execute_subtasks(subtasks)
    session.state.results = results
    
def Synthesizer(session):
    summarized = summarize(session.state.results)
    session.output = summarized
    