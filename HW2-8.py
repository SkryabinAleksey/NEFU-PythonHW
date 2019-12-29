def get_partition(S):
    list_s = list(set(S))
    List = []
    for i in range(len(list_s)):
        k_1 = S.find(list_s[i])
        k_2 = S.rfind(list_s[i])
        List.append([])
        c = 1
        for j in range(len(S)):
            if k_1 <= j <= k_2:
                List[i].append(c)
                c = c + 1
            else:
                List[i].append(0)
    New_List = []
    for i in range(len(S)):
        New_List.append(int(0))
        for j in range(len(list_s)):
            New_List[i] = int(New_List[i]) + int(List[j][i])
    m1 = 0
    Part_List = []
    for i in range(1, len(New_List)):
        if New_List[i] == 1:
            m2 = i
            Part_List.append(S[m1:m2])
            m1 = m2
    Part_List.append(S[m1:])
    return Part_List


if __name__ == '__main__':
    S = input("S = ")
    print(get_partition(S))