import markdown

def read_md(contents):
	start_index = contents.index("```python\n")
	end_index = contents.index("```\n")
	python_code = contents[start_index+1:end_index]
	python_code = "".join(python_code)

	md_code = contents[end_index+1:]
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
	week = raw_input("Week ID:")
	problem = raw_input("Problem ID:")
	input_file_name = "markdown_files/Week{0}_Problem{1}.md".format(week, problem)
	output_file_name = "output_files/Week{0}_Problem{1}.xml".format(week, problem)
	#input_file_name = "markdown_files/sample.md"
	#output_file_name = "output_files/sample_output.xml"
	template_file = "template_w_variables.xml"

	f = open(template_file, "r")
	template = f.readlines()
	f.close()

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