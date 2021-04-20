import json
import base64
import requests
import config

def run():
    oas = None
    base_path = None
    tags = []

    with open("open-api-specifications/gateway-v2.json") as json_file:
        oas = json.load(json_file)

    # defining base path
    base_path = "/api/am/gateway/v2"

    while True:
        print("\n" + "=" * len(config.portal_titles["gateway"]))
        print(config.portal_titles["gateway"])
        print("=" * len(config.portal_titles["gateway"]) + "\n")
        print("\nAvailable operations in Gateway Portal.")
        ops = []
        j = 1
        for path in oas["paths"]:
            for method in oas["paths"][path]:
                print("[%i] %s" % (j, oas["paths"][path][method]["summary"].strip()))
                ops.append({"path": path, "method": method})
                j += 1
        print("[%i] Back" % j)
        try:
            choice_for_op = int(input("\nChoose an option to continue: "))
            if choice_for_op < 1 or choice_for_op > len(ops) + 1:
                raise ValueError
            if choice_for_op == j:
                break
        except ValueError:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break
            else:
                continue
        print("\nDefine parameters under '%s'" %
              oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["summary"].strip())
        url = config.host + base_path + ops[choice_for_op - 1]["path"]
        params = {}
        for param in oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["parameters"]:
            if list(param.keys())[0] == "$ref":
                param = oas["parameters"][param["$ref"].split("/")[-1]]
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
        body = "{}"
        has_body = True if "requestBody" in oas["paths"][ops[choice_for_op - 1]["path"]][
            ops[choice_for_op - 1]["method"]].keys() else False
        if has_body:
            file_name = input("Enter file name having the request body* (json): ")
            try:
                fo = open(file_name)
                body = json.dumps(json.loads(fo.read()))
                fo.close()
            except:
                print("Invalid file.")
                input("\nPress enter to continue...")
                continue
        headers = {
            "Authorization": "Basic %s" % base64.b64encode(
                str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8"),
            "Content-Type": "application/json"
        }
        response = requests.request(ops[choice_for_op - 1]["method"], url, headers=headers, params=params,
                                    data=body, verify=False)
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
