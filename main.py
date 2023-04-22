import jira

def fetch_data(cred, filters = {}):
    
    server = cred['server']
    email_id = cred["email"]
    auth_token = cred["api_token"]
    
    jiraOptions = {'server': server}

    jira = JIRA(options=jiraOptions, basic_auth=(
    email_id, auth_token))
    
    fields = jira.fields()
    fields_dic = {}
    for field in fields:
        fields_dic[field['name']] = field['id']
    # print(fields_dic)
    
    
    # Search all issues mentioned against a project name.
    issue_dic = {"Issue_Type":[], "Project":[],"Status":[], "Story_Points":[], "Sprint":[], "Priority":[],
             "Assignee":[], "Issue_Key":[], "Description":[], "Summary":[], "Reporter":[]}
    
    jql_str = ""
    jql_str_list = []
    for i, filter in enumerate(filters.items()):
        if filter[1] != None:
            jql_str_list.append(f"\'{filter[0]}\'= \'{filter[1]}\'")
    l = len(jql_str_list)
    if l == 1:
        jql_str = jql_str_list[0]
    if l > 1:
        jql_str = jql_str_list[0]
        for fltr in jql_str_list[1:]:
            jql_str += " and " + fltr 
    print(jql_str)
    
    valid = True
    try:
        for singleIssue in jira.search_issues(jql_str=jql_str):
            break 
    except:
        valid = False
        
    if valid == False:
        return {"msg" : "Invalid Information Passed."}
      
    for singleIssue in jira.search_issues(jql_str=jql_str):
        try:
            Issue_Type = getattr(singleIssue.fields, fields_dic["Issue Type"]).name
        except:
            Issue_Type = None
        try:
            Project = getattr(singleIssue.fields, fields_dic["Project"]).name
        except:
            Project = None
        # try:
        #     Time_Spent = getattr(singleIssue.fields, fields_dic["Time Spent"])
        # except:
        #     Time_Spent = 0
        try:
            Status = getattr(singleIssue.fields, fields_dic["Status"]).name
        except:
            Status = "Backlog"
        try:
            Story_Points = getattr(singleIssue.fields, fields_dic["Story Points"])
        except:
            Story_Points = 0
        # try:
        #     Last_Viewed = getattr(singleIssue.fields, fields_dic["Last Viewed"])
        # except:
        #     Last_Viewed = None
        try:
            Sprint = getattr(singleIssue.fields, fields_dic["Sprint"])[0].name
        except:
            Sprint = None
        try:
            Priority = getattr(singleIssue.fields, fields_dic["Priority"]).name
        except:
            Priority = None
        try:
            Assignee = getattr(singleIssue.fields, fields_dic["Assignee"]).displayName
        except:
            Assignee = None
        try:
            Issue_Key = singleIssue.key
        except:
            Issue_Key = None
        try:
            Description = getattr(singleIssue.fields, fields_dic["Description"])
        except:
            Description = None
        try:
            Summary = getattr(singleIssue.fields, fields_dic["Summary"])
        except:
            Summary = None
        try:
            Reporter = getattr(singleIssue.fields, fields_dic["Reporter"]).displayName
        except:
            Reporter = None
        issue_dic["Issue_Type"].append(Issue_Type)
        issue_dic["Project"].append(Project)
        issue_dic["Time_Spent"].append(Time_Spent)
        issue_dic["Status"].append(Status)
        issue_dic["Story_Points"].append(Story_Points)
        issue_dic["Last_Viewed"].append(Last_Viewed)
        issue_dic["Sprint"].append(Sprint)
        issue_dic["Priority"].append(Priority)
        issue_dic["Assignee"].append(Assignee)
        issue_dic["Description"].append(Description)
        issue_dic["Summary"].append(Summary)
        issue_dic["Reporter"].append(Reporter)
        issue_dic["Issue_Key"].append(Issue_Key)

    return issue_dic
  
  cred = {"server" : "https://bhavin-sangani.atlassian.net", "email" : "100bhavinsangani@gmail.com", "api_token" : "ATATT3xFfGF0RIO9eXHFBzJHoPFVsFpEYcie7MSJwiSlvjsQRNO5EsOvJiL3WWQnHXV6Yb0bSbN0V_b0BEdhy7b4BBjH1UtPkyEyqiqvs-y_pHRmqBi8MdcH90jB8uTQcovNnZDHcV7HlYv7Jc_TI6h0zYt2E7LuVmeS-U699y87aBiHgC3ciM8=757265A8"}
  data = fetch_data(cred)
  print(data)
