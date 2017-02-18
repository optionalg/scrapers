import json

import ninetyninewaystofighttrump
import progressiveactiondaily
import twohoursaweek

if __name__ == "__main__":
    res1 = twohoursaweek.main()
    res2 = ninetyninewaystofighttrump.main()
    res3 = progressiveactiondaily.main()

    with open("results.json", "w") as f:
        f.write(json.dumps(res1 + res2 + res3))
