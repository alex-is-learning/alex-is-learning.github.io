---
layout: learning
title: "Bluedot AI Safety Journal Club, day 1"
topic: "AI Safety"
date: 2025-06-03
published: true
---

# Testing
Here's what I did

# Ended up with flashcards

<img src="/learning/2025-06-03%20bluedot/2025-06-03-bluedot-journal-club-1.png" alt="Bluedot Journal Club Day 1" style="display: block; max-width: 100%; height: auto; margin: 2em auto;" />

# Flashcards
And here are the flashcards:
{% raw %}
The name of the first paper I am reading for the Bluedot journal club is 
{{c1::Ctrl-Z: Controlling AI Agents via Resampling}}<br> | <br>
The first paper I'm reading for the Bluedot journal club was produced primarily by researchers at 
{{c1::Redwood Research}}<br> | <br>
and the 
{{c1::ML Alignment and Theory Scholars (MATS) Programme}}<br> | <br>
The research group most closely associated with The first bluedot paper is {{c1::Redwood Research}}<br> | <br>
The core threat model in The first bluedot paper is that of 
{{c1::subversive or untrusted LLM agents that may perform covert malicious actions while appearing helpful}}<br> | <br>
The first Bluedot paper proposes {{c1::a control evaluation wrapper}} rather than {{c1::changing the agent’s internal policy}}<br> | <br>
The main safety mechanism explored in the first Bluedot paper is 
{{c1::resampling suspicious agent outputs and selecting the least risky completion}}<br> | <br>
Resampling in control evaluations means 
{{c1::generating multiple outputs from the same agent query 
and choosing among them}}<br> | <br>
In AI safety, the goal of resampling is 
{{c1::to find a candidate that satisfies the user’s objective 
while avoiding risky or malicious behaviour}}<br> | <br>
In the first Bluedot paper, {{c1::resampling}} is combined with 
{{c1::a monitor that scores each candidate for danger}}, and the system {{c1::executes the lowest-risk option that still progresses the task}}<br> | <br>
Resampling preserves higher usefulness than {{c1::outright blocking}} because {{c1::the agent gets additional chances to propose a safe command}}<br> | <br>
Re: resampling looping:
{{c1::A basic resampling protocol may loop n times
requesting new outputs until either a safe candidate is found 
or the retry budget is exhausted}}<br> | <br>
Key hyper-parameters in resampling include (3 things)
{{c1::the number of retries, 
the monitor’s risk threshold, 
and the sampling temperature for diversity}}<br> | <br>
Sampling temperature is a hyper-parameter that adjusts 
{{c1::the randomness of a language model’s output}}<br> | <br>
Different temperature values in LLMs:
{{c1::temperature of 1 leaves the probability distribution unchanged, 
while T < 1 sharpens it 
and T > 1 flattens it}}<br> | <br>
Higher LLM temperature values lead to:
{{c1::increased diversity because lower-probability tokens become relatively more likely}}<br> | <br>
Excessively high LLM temperature can lead to 
{{c1::incoherent or off-topic completions due to over-randomness}}<br> | <br>
Typical LLM temperature ranges are 
{{c1::0.2–0.7}} for {{c1::factual precision}}<br> | <br>
and 
{{c1::0.8–1.2}} for {{c1::creative generation}}<br> | <br>
Setting temperature to 0 is equivalent to 
{{c1::always picking the single highest-probability token at each step}}<br> | <br>
The weakness of resampling is: 
{{c1::If the agent can anticipate the filter, 
resampling just returns multiple equally “stealthy” attacks 
instead of offering a safe alternative.}}<br> | <br>
(In-depth)
What it would look like for a malicious AI to get around resampling:
{{c1::It would tailor every variant to look harmless according to the monitor’s rules
E.g. avoiding obvious red-flag strings such as sudo, 
or split the malicious payload across several innocuous-looking commands.}}<br> | <br>
LLM resampling is most effective when combined with 
{{c1::a monitor that has low false negatives
so that dangerous outputs are reliably filtered away}}<br> | <br>
Resampling protocols trade {{c1::computational cost}} for safety; 
{{c1::more retries improve the chance of finding a safe command but incur higher latency}}<br> | <br>
The first bluedot paper introduces a benchmark called {{c1::BashBench}}<br> | <br>
The first bluedot paper creates a benchmark consisting of 
{{c1::257 real-world Unix StackExchange tasks}}<br> | <br>
In AI safety, a control evaluation is 
{{c1::an experimental test-bed 
that wraps an AI system in a safety layer 
and measures safety and usefulness together}}<br> | <br>
The control in control evaluation refers to 
{{c1::an external wrapper that supervises the AI}}<br> | <br>
rather than 
{{c1::changing the model’s internal weights}}<br> | <br>
The evaluation part of a control evaluation means 
{{c1::the protocol is empirically tested over many episodes and quantified, not just proposed in theory}}<br> | <br>
Key aim 1 of a control evaluation is 
{{c1::to minimise attack success rate, i.e. how often malicious actions slip through}}<br> | <br>
Key aim 2 of a control evaluation is 
{{c1::to maximise usefulness, i.e. how much legitimate task performance the AI retains}}<br> | <br>
A typical control evaluation leaves {{c1::the base model untouched}} and focuses entirely on {{c1::the behaviour of the outer wrapper}}<br> | <br>
Common ingredients of a control evaluation include (4 things)
{{c1::an environment, 
a defined threat model, 
a control protocol, 
and metrics}}<br> | <br>
The environment in a control evaluation gives the agent real tools, such as {{c1::a Bash shell}} or {{c1::web browser}}, to allow meaningful tasks and potential harm<br> | <br>
The {{c1::threat model}} in a control evaluation specifies 
{{c2::what counts as an attack, e.g. malware download or data exfiltration}}<br> | <br>
In a control evaluation, the {{c1::control protocol}}, also called {{c1::the wrapper}}, monitors 
{{c2::proposed actions, blocks or amends risky ones, and may resample alternatives}}<br> | <br>
Metrics in control evaluations are often plotted as a 
{{c1::safety–usefulness trade-off curve}}<br> | <br>(add image!)<br> | <br>
Control evaluations complement {{c1::preventive}} alignment methods such as {{c1::RLHF}} by acting as a defence-in-depth layer<br> | <br>
Unlike internal alignment work, control evaluations assume 
{{c1::the model could already be malicious and test whether external supervision is enough}}<br> | <br>
Control evaluations typically run {{c1::thousands of adversarial episodes to gather statistically robust results}}<br> | <br>
Examples of control evaluation metrics include 
{{c1::attack success percentage}}<br> | <br>
and 
{{c1::task completion rate under the wrapper}}<br> | <br>
Control evaluations can involve 
{{c1::a weaker trusted model}} or<br> | <br>
{{c1::human auditor}}<br> | <br>
to help judge the safety of the agent’s actions<br> | <br>
A control evaluation seeks a wrapper that 
{{c1::drives attack success towards zero}}<br> | <br>
while 
{{c1::keeping usefulness as high as possible}}<br> | <br>
A single-step control evaluation asks an AI to 
{{c1::produce one output once}}<br> | <br>
which is 
{{c1::judged for safety and usefulness}}<br> | <br>
{{c1::Greenblatt 2023}} is a classic example of single-step control evaluation<br> | <br>
An environment is called state-ful when 
{{c1::that data changes as you interact with it 
and those changes remain in effect for later steps}}<br> | <br>
A multi-step agent episode lets the AI 
{{c1::issue repeated actions in a stateful environment}},<br> | <br>
such as 
{{c1::10–15 Bash commands in sequence}}<br> | <br>
The first Bluedot journal's key innovation:
{{c1::extends control evaluations from single-step to multi-step agent episodes}}<br> | <br>
In a multi-step AI setting cumulative risk grows because 
{{c1::even a small per-step failure rate compounds over many actions}}<br> | <br>
Multi-step episodes enable {{c1::temporal attack}} strategies, where 
{{c1::an agent behaves innocently for several steps before striking}}<br> | <br>
Stateful side-effects matter in multi-step control because 
{{c1::early commands can set up conditions that later commands exploit}}<br> | <br>
Example of a multi-step task in Ctrl-Z: 
{{c1::setting up password-less SSH 
by issuing several sequential shell commands}}<br> | <br>
Previous control-evaluation work {{c1::tested single-step tasks}}, whereas<br> | <br>
the first bluedot paper 
{{c1::moves to multi-step agent episodes}}<br> | <br>
On BashBench,
an unprotected agent achieves {{c1::58}}% attack success,<br> | <br>
which the first bluedot paper reduces to {{c1::7}}%<br> | <br>
with its best protocol<br> | <br>
The usefulness cost of the best "first Bluedot journal club" paper protocol is 
{{c1::only about 5 % relative drop in task completion when the agent is honest}}<br> | <br>
In the first bluedot paper setup 
each episode may include 
{{c1::up to 15 shell commands issued by the agent}}<br> | <br>
The monitoring component in the first bluedot paper can be 
{{c1::a smaller trusted model that rates each command’s risk}}<br> | <br>
Re: AI
{{c1::Defer-to-trusted}} means<br> | <br>
{{c2::handing a suspected command to a trusted baseline policy}},<br> | <br>
whereas {{c1::Defer-to-resample}}<br> | <br>
{{c2::asks the main model for alternative outputs}}<br> | <br>
Resampling improves the usefulness–safety Pareto frontier compared with {{c1::simply blocking all flagged commands}}<br> | <br>
The first bluedot paper budgets {{c1::human audits}} for only about {{c1::1}}% of steps,<br> | <br>
showing that 
{{c1::the protocol can work with limited human oversight}}<br> | <br>
In the first bluedot paper,
the agent interacts through 
{{c1::a bash shell environment}}, giving realistic system-level capabilities<br> | <br>
The first bluedot journal paper positions {{c1::control evaluations}} as complementary to {{c1::preventive alignment techniques such as RLHF}}<br> | <br>
Control evaluations assume that
{{c1::the model could be fully malicious}},<br> | <br>
so they belong to the 
{{c1::defence in depth}} layer of AI safety<br> | <br>
A key novelty of The first bluedot paper is demonstrating that 
{{c1::resampling need not sacrifice much task performance}} while<br> | <br>
{{c1::greatly improving safety}}<br> | <br>
Attack success in the first bluedot paper is defined as 
{{c1::the agent executing a command that matches a malicious reference set}}<br> | <br>
Usefulness in the first bluedot paper is measured by 
{{c1::whether the agent achieves the task’s ground-truth goal without hazardous behaviour}}<br> | <br>
The BashBench tasks were filtered so that 
{{c1::a single command could accomplish the user’s goal}}, creating<br> | <br>
{{c1::a clear malicious versus benign distinction}}<br> | <br>
Lower risk scores in The first bluedot paper are associated with commands that 
{{c1::lack indicators such as network downloads, chmod +x, or sudo}}<br> | <br>
When monitoring is perfect, The first bluedot paper shows a theoretical upper bound where 
{{c1::attack success approaches zero at zero human cost}}<br> | <br>
{% endraw %}