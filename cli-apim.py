import json
import base64
import requests
import config
import auth

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def run(portal):
    oas = None
    base_path = None
    tags = []

    with open("open-api-specifications/%s-v2.json" % portal) as json_file:
        oas = json.load(json_file)

        # defining base path
        base_path = "/api/am/%s/v2" % portal

        # listing tags
        for path in oas["paths"]:
            for method in oas["paths"][path]:
                for tag in oas["paths"][path][method]["tags"]:
                    if tag not in tags:
                        tags.append(tag)

    while True:
        print("\n" + "=" * len(config.portal_titles[portal]))
        print(config.portal_titles[portal])
        print("=" * len(config.portal_titles[portal]) + "\n")
        print("You can choose operations under following categories.")
        i = 1
        for tag in tags:
            print("[%i] %s" % (i, tag.strip()))
            i += 1
        print("[%i] Back" % i)
        try:
            choice_for_tag = int(input("\nChoose an option to continue: "))
            if choice_for_tag < 1 or choice_for_tag > len(tags) + 1:
                raise ValueError
        except ValueError:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break
            else:
                continue
        if choice_for_tag == i:
            break
        print("\nOperations under '%s'" % tags[choice_for_tag - 1])
        ops = []
        j = 1
        for path in oas["paths"]:
            for method in oas["paths"][path]:
                for tag in oas["paths"][path][method]["tags"]:
                    if tag == tags[choice_for_tag - 1]:
                        print("[%i] %s" % (j, oas["paths"][path][method]["summary"].strip()))
                        ops.append({"path": path, "method": method})
                        j += 1
        print("[%i] Back" % j)
        try:
            choice_for_op = int(input("\nChoose an option to continue: "))
            if choice_for_op < 1 or choice_for_op > len(ops) + 1:
                raise ValueError
        except ValueError:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break
        if choice_for_op == j:
            continue
        print("\nDefine parameters under '%s'" %
              oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["summary"].strip())
        url = config.host + base_path + ops[choice_for_op - 1]["path"]
        params = {}
        for param in oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["parameters"]:
            if list(param.keys())[0] == "$ref":
                param = oas["components"]["parameters"][param["$ref"].split("/")[-1]]
            is_required = True if "required" in param.keys() and param["required"] else False
            param_type = param["schema"]["type"] if "schema" in param.keys() else param["type"]
            params[param["name"]] = input(
                "Enter %s%s (%s): " % (param["name"], "*" if is_required else "", param_type))
        param_keys = list(params.keys())
        for param in param_keys:
            if params[param] == '':
                del params[param]
            elif param in url:
                url = url.replace("{" + param + "}", params[param])
        if portal == "gateway":
            headers = {
                "Authorization": "Basic %s" % base64.b64encode(
                    str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8"),
                "Content-Type": "application/json"
            }
        else:
            scopes = " ".join(
                oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["security"][0][
                    "OAuth2Security"])
            headers = {
                "Authorization": "Bearer %s" % auth.get_access_token(scopes)
            }
        response = requests.request(ops[choice_for_op - 1]["method"], url, headers=headers, params=params,
                                    verify=False)
        print()
        if response.status_code == 200:
            try:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            except:
                print(
                    "\033[1;31mError occured while decoding json object. Check whether you are using correct API "
                    "version.\033[0;37m")
        else:
            print(response)
        input("\nPress enter to continue...")


def start():
    while True:
        print("\n====================================")
        print("CLI for WSO2 API Manager RESTful API")
        print("====================================\n")
        print("You can access following RESTful APIs.")
        print("[1] WSO2 Publisher v2\n"
              "[2] WSO2 Developer Portal v2\n"
              "[3] WSO2 Admin Portal v2\n"
              "[4] WSO2 Gateway API v2\n"
              "[5] Exit\n")
        choice_for_api = input("Choose the API you want to access: ")
        if choice_for_api == "1":
            run("publisher")
        elif choice_for_api == "2":
            run("devportal")
        elif choice_for_api == "3":
            run("admin")
        elif choice_for_api == "4":
            run("gateway")
        elif choice_for_api == "5":
            break
        else:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break


start()
