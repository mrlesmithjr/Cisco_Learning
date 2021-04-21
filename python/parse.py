#!/usr/bin/env python

# import json
import logging

# import pprint
from genie.testbed import load

LOG_STDOUT = False
TESTBED = "devnet_sbx_testbed.yml"


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    testbed = load(TESTBED)
    # learnt = {}
    for name, dev in testbed.devices.items():
        dev.connect(log_stdout=LOG_STDOUT)
        # ospf = dev.learn("ospf")
        # print(ospf)
        # learnt[name] = {}
        # learnt[name]["version"] = dev.parse("show version")
        # learnt[name]["running_config"] = dev.parse("show running-config")
        # learnt[name]["bgp"] = dev.learn("bgp")
        # ospf = dev.learn("ospf")
        # learnt[name]["ospf"] = dev.parse(ospf)

    # print(json.dumps(learnt))


if __name__ == "__main__":
    main()
