import markdown
import json
import sys

def read_md(contents):
	start_index = contents.index("```python\n")
	end_index = contents.index("```\n")
	python_code = contents[start_index+1:end_index]
	python_code = "".join(python_code)

	md_code = contents[end_index+1:]
	html_code = markdown.markdown("".join(md_code))

	f.close()
	return python_code, html_code

def read_md_new(contents):
	start_index = contents.index("```python\n")
	end_index = contents.index("```\n")
	python_code = contents[start_index+1:end_index]
	python_code = "".join(python_code)

	md_code = contents[end_index+1:]
	inline = 0
	double = 0
	inlineSub = ['\\\\\\(', '\\\\\\)']
	doubleSub = ['\\\\\\[', '\\\\\\]']
	for j in xrange(len(md_code)):
		line = md_code[j]
		line = line.replace('\\$','\001')
		i=0
		while i < len(line):
			if line[i:i+2] == '$$':
				line = line[:i]+doubleSub[double]+line[i+2:]
				double = 1-double
				i += 4
				continue
			if line[i] == '$':
				line = line[:i]+inlineSub[inline]+line[i+1:]
				inline = 1-inline
				i += 4
				continue
			i += 1
		line = line.replace('\001','$')
		md_code[j] = line
	html_code = markdown.markdown("".join(md_code))

	f.close()
	return python_code, html_code

def convert_html(html_code, template):
	html_code = html_code.splitlines()
	start_index = template.index('    <customresponse cfn="check" expect="\\[$solution1\\]">\n')
	end_index = start_index+4
	answer_box_xml_code = template[start_index:end_index]
	template = template[:start_index] + template[end_index:]
	updated_html_code = []
	part_id = 1
	for line in html_code:
		if '<p>[_]</p>' == line:
			updated_html_code += ['\n', '\n']
			xml_code = answer_box_xml_code[0].replace('solution1', 'solution'+str(part_id))
			updated_html_code.append(xml_code)
			updated_html_code += answer_box_xml_code[1:]
			updated_html_code += ['\n', '\n']
			part_id += 1
		else:
			updated_html_code.append(line)
	updated_html_code = "".join(updated_html_code)
	template.insert(start_index, updated_html_code)
	return template




if __name__ == "__main__":
	if sys.argv[1] == "--help":
		print "Please type in parameters as follow:"
		print "python translate.py <Week ID> <Problem ID>"
		sys.exit()

	try:
		week,problem= sys.argv[1:]
	except:
		sys.exit("Error, see 'python translate.py --help' for input requirement")
	#week = raw_input("Week ID:")
	#problem = raw_input("Problem ID:")
	mapping = json.loads(open("problems_mapping.json").read())
	mapping_key = "Week{0}_Problem{1}".format(week, problem)
	file_name = mapping[mapping_key]
	input_file_name = "problem_source_files/{0}.md".format(file_name)
	output_file_name = "problem_XML_files/{0}.xml".format(mapping_key)
	template_file = "template.xml"

	f = open(template_file, "r")
	template = f.readlines()
	f.close()

	# input_file_name = 'test.md'
	# output_file_name = "{0}.xml".format(mapping_key)
	f = open(input_file_name, "r")
	contents = f.readlines()
	f.close()

	print "generating XML"

	py_code, html_code = read_md(contents)
	template.insert(4, py_code)
	template = convert_html(html_code, template)

	print "writing files ..."

	f = open(output_file_name, "w")
	f.write("".join(template))
	f.close()

	print "Done! XML files saved in output_files folder!"