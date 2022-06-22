account={"acc_no":1000,"acc_branch":"kalamassery","acctype":"savings","balance":5000}
print(account)
print(account["acctype"])
account["balance"]+=1000
print(account)
print(account.get("acc_branch"))

