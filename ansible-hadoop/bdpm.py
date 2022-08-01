import sys, os

HOME_PATH='/ansible/ansible-hadoop'

def print_usage():
    print('illegal arguments')


if __name__ == '__main__':
    # argv filter
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(2)

    def parse_args(component, act):
        return (component, act)
    
    # inventories/host.yaml
    inventory = 'host' 
    component, act = parse_args(*sys.argv[1:])

    # make ansible-playbook command
    # ansible-playbook -i <inventory-file> <playbook-file>
    command = ' '.join([
        'ansible-playbook',
        # inventory
        f'-i {HOME_PATH}/inventories/{inventory}.yml',
        # playbook
        f'{HOME_PATH}/{component}.yml',
        # extra vars
        f'--extra-vars "act={act}"'
    ])

    # execute ansible playbook
    print(os.system(command))