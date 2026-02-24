def merge_the_tools(string, k):
   for i in range(0, len(string), k):
        ti = string[i : i + k]
        ui = ""
        for char in ti:
            if char not in ui:
                ui += char
        print(ui)
