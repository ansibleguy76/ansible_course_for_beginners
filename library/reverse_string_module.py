#!/usr/bin/python

# Copyright: (c) 2020, Ansibleguy76

# This custom module will reverse a string and optionally capitalize the string.

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule


# main code
def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        input                     = dict(type='str', required=True),
        is_capitals               = dict(type='bool', default=False) 
    )

    # seed the result dict in the result object
    result = dict(
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # store input to vars, some are global
   
    input                  = module.params['input']
    is_capitals            = module.params['is_capitals']
   
    reversed = input[::-1]
    if is_capitals:
        reversed = reversed.upper()


    result["changed"] = False # choose here if you want the module to register a change
    result["output"] = reversed


    # return
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()