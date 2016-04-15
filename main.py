import stackexchange

print("Getting information from dumps. Please, wait, it\'s going to take nearly 1 minute.")
questions, result = stackexchange.getQuestions("Comments.xml", "Posts.xml", "Users.xml")
questions = sorted(questions)
print("Enter output file name without an extension: ", end="")
filename = input()
while filename == '':
    print("Please, enter non-empty string: ", end="")
    filename = input()
output = open(filename + ".html", "w")
output.write('<html>\n<head>\n<title>Questions in codereview.stackexchange.com</title>\n</head>\n<body>\n<ul>\n')
output.write('<header>\n<h1>Maximum number of "good" comments for one question is ' + str(result) + '. Here is the list of all questions, that have such number of "good" comments: </h1>\n</header>')
for question in questions:
    output.write('<li><a href="https://codereview.stackexchange.com/questions/' + str(question) +'">' + 'Question ' + str(question) + '</a> has ' + str(result) + ' comments posted between midnight and 6 a.m. by people with reputation over 100.</li>\n')
output.write('</ul>\n</body>\n</html>')
print("Done")
output.close()