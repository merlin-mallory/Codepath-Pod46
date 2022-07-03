import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        '''
        There is an infrastructure of n cities with some number of roads connecting these cities.
        Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

        The network rank of two different cities is defined as the total number of directly connected roads to either
        city. If a road is directly connected to both cities, it is only counted once.

        The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

        Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

        Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
        Output: 4
        Explanation:
        The network rank of cities 0 and 1 is
        4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

        Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
        Output: 5
        Explanation: There are 5 roads that are connected to cities 1 or 2.

        Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
        Output: 5
        Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

        Constraints:
        2 <= n <= 100
        0 <= roads.length <= n * (n - 1) / 2
        roads[i].length == 2
        0 <= ai, bi <= n-1
        ai != bi
        Each pair of cities has at most one road connecting them.

        Plan:
        1. Create a dictionary that will contain a list that contains a count of all of the roads connected to that
        city, and a list of the indexes of connected cities.
        2. Loop through roads and construct the dictionaries.
        3. Create a helper function that will calculate the maximal rank by counting the number of roads emenating
        from the max city node and the max city's children.
        4. Find the city that has the maximum number of attached cities. Calculate and return the maximal rank using
        that node.
        5. Time: O(n*r), Space: O(n*r)
        '''

        city_to_cities = [set() for i in range(n)]
        max_network_rank = 0
        for road in roads:
            city_to_cities[road[0]].add(road[1])
            city_to_cities[road[1]].add(road[0])
        for city_1 in range(n):
            for city_2 in range(city_1 + 1, n):
                network_rank = len(city_to_cities[city_1]) + len(city_to_cities[city_2])
                if (city_1 in city_to_cities[city_2]):
                    network_rank -= 1
                max_network_rank = max(max_network_rank, network_rank)
        return max_network_rank
    #
#         from collections import defaultdict
#
#         city_count_dict = collections.defaultdict(int)
#         city_connect_dict = collections.defaultdict(list)
#
#         for road in roads:
#             left, right = road[0], road[1]
#             # if right not in city_connect_dict[left]:
#             city_connect_dict[left].append(right)
#
#             # if left not in city_connect_dict[right]:
#             city_connect_dict[right].append(left)
#
#             city_count_dict[left] += 1
#             city_count_dict[right] += 1
#
#         max_city_index_list = []
#         max_city_count = -1
#
#         for key in city_connect_dict:
#             if len(city_connect_dict[key]) > max_city_count:
#                 max_city_index_list = [key]
#                 max_city_count = len(city_connect_dict[key])
#             elif len(city_connect_dict[key]) == max_city_count:
#                 max_city_index_list.append(key)
#
#         def calculate_maximal_rank(max_city_index):
#             connected_children_list = city_connect_dict.get(max_city_index)
#             print("connected children list:", connected_children_list)
#             road_count = 0
#
#             selected_city = None
#             current_max = -1
#
#             for city in connected_children_list:
#                 if city_count_dict.get(city) > current_max:
#                     current_max = city_count_dict.get(city)
#                     selected_city = city
#
#             road_count += len(city_connect_dict[max_city_index])
#             road_count += len(city_connect_dict[selected_city]) - 1
#
#             # visited_set = set()
#             # for city in connected_children_list:
#             #     visited_set.add(city)
#             #     for connection in city_connect_dict[city]:
#             #         if connection not in visited_set:
#             #             road_count += 1
#
#             print("calc func with", max_city_index, "is returning", road_count, "roads")
#             return road_count
#
#         current_max_city_count = -1
#         current_max_city_index = -1
#
#         for city in max_city_index_list:
#             this_city_count = calculate_maximal_rank(city)
#             if this_city_count > current_max_city_count:
#                 current_max_city_count = this_city_count
#                 current_max_city_index = city
#
#         print("end max city index:", current_max_city_index)
#         print("end max city values from dict:", city_connect_dict[current_max_city_index])
#         print("end connect dict keys:", city_connect_dict.keys())
#         print("end connect dict values:", city_connect_dict.values())
#         print("end count dict keys:", city_count_dict.keys())
#         print("end count dict values:", city_count_dict.values())
#         return current_max_city_count
#
# obj = Solution()
#
# # roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# # result = obj.maximalNetworkRank(8, roads) # expect 4
# #
# roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
# result = obj.maximalNetworkRank(4, roads) # expect 4
#
# # roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# # result = obj.maximalNetworkRank(5, roads) # expect 5
#
# print(result)
