import sys, re, os, traceback
from .transform import transform
from .errorHandle import error

def pars(script):
    scriptL = script.split("\n")
    final = ""
    for s in scriptL:
        def replace(match):
            keyword = match.group(1)
            if match.group(2) is not None or match.group(3) is not None:
                # Match is inside quotes, return the original match
                return match.group(0)
            else:
                # Match is not inside quotes, perform the replacement
                try:
                    return transform[keyword]
                except:
                    return keyword

        # Define the regular expression pattern to match the keywords
        pattern = r'\b(' + '|'.join(map(re.escape, transform.keys())) + r')\b|("[^"]*")|(\'[^\']*\')'

        # Use re.sub() with the lambda function to perform the replacements
        result = re.sub(pattern, replace, s)
        # pattern = '|'.join(map(re.escape, transform.keys()))
        # # pattern = r"\b(" + "|".join(map(re.escape, transform.keys())) + r")\b(?=(?:(?<!\\)['\"][^'\"]*(?<!\\)['\"])|$)"
        # result = re.sub(pattern, lambda match: transform[match.group(0)], s)
        #print(result)
        final += f"{result}\n"
    return final

def pars_mbalek(script): # transform back for the error handling
    transform_ = {value: key for key, value in transform.items()}
    scriptL = script.split("\n")
    final = ""
    for s in scriptL:
        def replace(match):
            keyword = match.group(1)
            if match.group(2) is not None or match.group(3) is not None:
                return match.group(0)
            else:
                try:
                    return transform_[keyword]
                except:
                    return keyword
        pattern = r'\b(' + '|'.join(map(re.escape, transform_.keys())) + r')\b|("[^"]*")|(\'[^\']*\')'
        result = re.sub(pattern, replace, s)
        final += f"{result}\n"
    return final

def raiseError(s):
    try:
        s = f'{pars_mbalek(str(s).split("^")[0]+"^")}{str(s).split("^")[1]}'
    except:
        s = str(s)
    pattern = '|'.join(map(re.escape, error.keys()))
    result = re.sub(pattern, lambda match: error[match.group(0)], s, flags=re.IGNORECASE)
    print(result.replace("<string>", sys.argv[2]))

def main():
    try:
        if sys.argv[1] == 'run':
            try:
                path_ = sys.argv[2]
                if os.path.isfile(sys.argv[2]):
                    with open(sys.argv[2], 'r') as rr:
                        exec(pars(rr.read()))
                else:
                    raise Exception("file ora ditemokake cuk!")
            except Exception as e:
                e = traceback.format_exc()
                #print(e)
                raiseError(e)
    except Exception as e:
        #print(e)
        print("Use `jawalang run <path>` to execute file")