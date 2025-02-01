from jinja2 import Template

statement1 = Template("IIT Madras provides diploma in {{Value_1}} {{Value_2}}")
statement2 = Template("IIT Madras provides degree in {{Value_1}}{{Value_2}}")

out1 = statement1.render(Value_1="programming")
out2 = statement2.render(Value_2="data science")
print(out1)
print(out2)
