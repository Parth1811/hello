    import numpy as np
    from copy import deepcopy

    CODE_TABLE = np.array([-1]*10)

    class Node:
        def __init__(self, name, next_node0 = None, next_node1 = None, prev_node = None, weight = 0, value = 0):
            self.name = name
            self.next_node0 = next_node0
            self.next_node1 = next_node1
            self.prev_node = prev_node
            self.weight = weight
            self.value = value

        def get_code(self):
            code = str(self.weight)
            while self.prev_node != None:
                self = self.prev_node
                code = str(self.weight) + code
            return code


    def get_freq_distribution(s):
        FREQ_DIST = np.zeros((10,1))
        for letter in s:
            FREQ_DIST[int(letter)] += 1

        return FREQ_DIST

    def create_base_nodes(FREQ_DIST):
        node_list = []
        for i, freq in enumerate(FREQ_DIST):
            if freq != 0:
                node_list.append(Node(str(i), value = freq))
        return node_list

    def make_a_tree(node_list):
        if len(node_list) <= 1:
            return node_list

        min1, min2 = 0, 0    #min1 <= min2
        min1_index, min2_index = -1, -1
        for i, node in enumerate(node_list):
            if node.value < min2:
                if node.value < min1:
                    min2, min1  = min1, node.value
                    min2_index, min1_index = min1_index, i
                else:
                    min2  = node.value
                    min2_index = i

        #Merge two nodes
        new_node = Node(
            name= node_list[min1_index].name + node_list[min2_index].name,
            next_node0 = node_list[min1_index],
            next_node1 = node_list[min2_index],
            value= node_list[min1_index].value + node_list[min2_index].value
        )

        node_list[min1_index].weight, node_list[min1_index].prev_node = 0, new_node
        node_list[min2_index].weight, node_list[min2_index].prev_node = 1, new_node

        node_list.pop(min1_index)
        node_list.pop(min2_index)
        node_list.append(new_node)


        return make_a_tree(node_list)

    def print_output(node_list):
        if len(node_list) == 0:
            return

        next_node_list = []
        for node in node_list:
            for i in range(10):
                if node.name == str(i):
                    CODE_TABLE[i] = node.get_code()
            if node.next_node0 != None:
                next_node_list.append(node.next_node0)
                next_node_list.append(node.next_node1)

        print_output(next_node_list)
        return


if __name__ == '__main__':
    s = '1751709618360459813571045'
    base_ndoe_list = create_base_nodes(get_freq_distribution(s))
    print base_ndoe_list
    make_a_tree(base_ndoe_list)
    print_output(base_ndoe_list)
    for i, code in enumerate(CODE_TABLE):
        if code == -1:
            print (str(i) + ' null')
        else:
            print (str(i) + ' ' + str(code))
