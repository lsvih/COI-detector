import argparse
import requests
import xml.etree.ElementTree as ET


def fetch_coauthor_from_dblp(dblp_id):
    print('Fetching coauthors from DBLP...')
    author_xml = requests.get('https://dblp.org/pid/{}.xml'.format(dblp_id)).text
    root = ET.fromstring(author_xml)
    coauthor_list = [coa.text for coa in root.findall('coauthors/co/na')]
    print('Found {} coauthors for {}.'.format(len(coauthor_list), dblp_id))
    return coauthor_list


def check():
    coa_list = fetch_coauthor_from_dblp(args.dblp_id)
    pc_list = open(args.pc_list).read().strip().splitlines()
    conflict_list = []
    for pc in pc_list:
        for coa in coa_list:
            if all(t in coa.lower().split() for t in pc.lower().split()):
                conflict_list.append(pc)
                break
        else:
            continue
    print('Found {} conflicts.'.format(len(conflict_list)))
    print('Possible conflict list:')
    for conflict in conflict_list:
        print(conflict)
    open(args.output, 'w').write('\n'.join(conflict_list))
    print('Possible COIs list saved to {}.'.format(args.output))


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--pc_list', type=str, default='pc_list.txt')
    arg_parser.add_argument('--dblp_id', type=str, default='233/1228')
    arg_parser.add_argument('--output', type=str, default='coi.txt')
    args = arg_parser.parse_args()
    check()
