class Solution():
    def method(self, list_of_word):
        chara_index = 0
        public_pre = []
        if list_of_word == []:
            return ""
        elif len(list_of_word) == 1:
            return list_of_word[0]
        else:
            if_exec = True
            while if_exec:
                for i in range(0,len(list_of_word)):
                    if len(list_of_word[i]) < chara_index+1 and i == 0:
                        if_exec = False
                        break
                    elif len(list_of_word[i]) < chara_index+1 and i > 0:
                        public_pre = public_pre[:-1]
                        if_exec = False
                        break
                    elif len(public_pre) < chara_index+1:
                        public_pre.append(list_of_word[i][chara_index])
                    elif list_of_word[i][chara_index] != public_pre[chara_index]:
                        public_pre = public_pre[:-1]
                        if_exec = False
                        break
                chara_index += 1
            return "".join(public_pre)

if __name__=="__main__":
    sol = Solution()
    print(sol.method(["dog","racecar","car"]))


