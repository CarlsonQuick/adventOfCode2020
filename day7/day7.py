class Bag():
    def __init__(self, count, color):
        self.count = count
        self.color = color
        self.children = set()
    def add_child(self, child):
        self.children.add(child)
    def fits(self, target_color):
        for child in self.children:
            if child.color == target_color:
                return True
        return False

    def __repr__(self):
        return self.color
    def __str__(self):
        child_str = 'Children: '
        for child in self.children:
            child_str += ' ' + child.color, child.count
        return '{0},{3} {1} {2}'.format(self.color, len(self.children), child_str, self.count)
#not 56

def get_child_attr(phrase):
    phrase = phrase.strip()
    words = phrase.split(' ')
    count = int(words[0])
    color = '{0} {1}'.format(words[1], words[2])
    return Bag(count=count, color=color)

def count_children(rules, target_color):
    sum = 1
    for bag in rules:

        if bag.color == target_color:
            print(' in ', target_color)
            for c in bag.children:
                child_bags = count_children(rules, c.color)
                print(c.count, c.color, ' bags with ', child_bags, ' in them')
                sum += c.count * child_bags
    return sum


def count_parents(rules, target_color):
    valid_path = set()
    paths = []
    for bag in rules:
        if bag.fits(target_color=target_color):
            paths.append('{0},{1}'.format(target_color, bag.color))
            valid_path.add(bag)

    nested_paths = set()
    for bag in valid_path:
        valid_child_paths = count_parents(rules, bag.color)
        for cp in valid_child_paths:
            paths.append('{0},{1}'.format(target_color,cp))


    return paths

with open('input.txt') as f:
    rules = []
    for line in f:
        split_line = line.split(' bags contain ')
        new_bag = split_line[0]
        children = []

        if split_line[1].find('no other bags') >=0:
            children = [] #no valid children
        elif split_line[1].find(',') >=0:
            for phrase in split_line[1].split(','):
                children.append(get_child_attr(phrase=phrase))

        else:
            children.append(get_child_attr(split_line[1]))
            #parse multiple bags

        bag = Bag(1, new_bag)
        for child in children:
            bag.add_child(child)
        rules.append(bag)
count = count_children(rules, 'shiny gold')
print(count-1)
# btchb = count_parents(rules, 'shiny gold')
# unique_parents = set()
# for b in btchb:
#     path = b.split(',')
#     path.reverse()
#     unique_parents.add( path[0])
#
#     print(b)
#
#
#
# print(len(btchb))
# print(len(unique_parents), unique_parents)

# for rule in rules:
#     print(rule.color, rule.count, rule.children)


