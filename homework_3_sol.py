# Problem 1-1

for i in range(5):
    print("{:^9}".format("*" * (2 * i + 1)))


# Problem 1-2

for i in range(5):
    for _ in range(5 - (i + 1)):
        print(" ", end="")
    for _ in range(2 * i + 1):
        print("*", end="")
    print("")


# Problem 2
sample_str = 'ABCABAAB'
c = "A"

index_lst = []

for i, s in enumerate(sample_str):
    if c == s:
        index_lst.append(i)

print(index_lst)

# # Problem 3
# import random
# random_num = random.randint(1, 100)
# print(random_num)
#
# trial_cnt = 0
# while True:
#     input_num = int(input("input number : "))
#     trial_cnt += 1
#
#     if input_num == random_num:
#         print("맞췄습니다.")
#         print(trial_cnt, "번 만에 맞췄습니다.")
#         break
#     elif input_num < random_num:
#         print("낮습니다.")
#     else:
#         print("높습니다.")


# Problem 4
news_str = """
Kim Jong Un is sending his younger sister to South Korea for the Winter Olympics, the first time any member of the Kim dynasty has visited the country.

South Korea's Unification Ministry said in a statement that Kim Yo Jong will be joining North Korea's high-level delegation to the South, headed by Kim Yong Nam, president of North Korea's parliament.
The 30-year-old, who has seen her profile rise steadily since 2014, was last year promoted to North Korea's Politburo. She and Kim Jong Un were born to the same mother, Ko Yong Hui.
Kim Yo Jong's inclusion in the North Korean delegation is likely to irritate the United States, which has sent its own delegation led by Vice President Mike Pence to counter North Korea's charm offensive.
Last year, the US Treasury Department included Kim Yo Jong on its list of blacklisted officials. As the vice director of the Workers' Party Propaganda and Agitation Department, she has been targeted by US sanctions.
On a refueling stop on his way to Asia, Pence said the aim of his trip was to show American "resolve" in rallying the international community against the Kim regime.
"We're traveling to the Olympics to make sure that North Korea doesn't use the powerful symbolism and the backdrop of the Winter Olympics to paper over the truth about their regime," Pence said.

But South Korea welcomed the announcement, saying it was "significant that Kim had included his sister in the delegation.
"We believe that the North's announcement of the delegation shows its willingness to ease tensions on the Korean peninsula along with a message of celebration for the PyeongChang Olympic Winter Games," it said in a statement. "It is significant that the delegation also includes Kim Yo Jong, who is Chairman Kim Jong Un's sister and holds an important position in the Workers' Party of Korea."
Hopes for a breakthrough
Kim's presence, alongside Kim Yong Nam (no relation), the 90-year-old ceremonial head of state in North Korea, will raise hopes for a potential breakthrough in relations with the US.
This week, Pence suggested he would be open to meeting North Korean politicians on the sidelines of the Olympics, saying President Donald Trump "always believes in talking."
"North Korea can have a better future than the militaristic path, the path of provocation and confrontation that it's on. Better for its own people, better for the region, and better for peace," Pence said.
However on Wednesday he also warned the US was about to impose the "toughest and most aggressive round of economic sanctions on North Korea ever."
"We will continue to isolate North Korea until it abandons its nuclear and ballistic missile programs once and for all," he said.
The Vice President's delegation includes the father of the late Otto Warmbier, an American student who died shortly after being released from North Korean custody.
Fred Warmbier and his wife Cindy were in the audience during US President Donald Trump's State of the Union address last month.
They looked on tearfully as the President cited their son's treatment as a example of the "menace that threatens our world."
The US delegation will be joined by the President's daughter and senior advisor Ivanka Trump, who will attend the closing ceremony on February 25, a White House official said Monday.
Hundreds of North Koreans have arrived in South Korea ahead of the Opening Ceremony on Friday.
Though only 22 athletes will compete in events, the North's delegation will be among the largest at the Games.
It includes an 114-strong art troupe and 96-crew who arrived at South Korea's Mukho port on Wednesday aboard the Mangyongbong 92 cargo-passenger ferry.
Who is North Korean pop star Hyon Song Wol?

Who is North Korean pop star Hyon Song Wol? 02:44
Kim's delegation includes Hyon Song Wol, the lead singer of Kim Jong Un's favorite girl band, whose every move was followed by a insatiable South Korean press during a pre-Games tour last month.
Hyon's the closest thing North Korea has to a celebrity and her presence in Pyeongchang is an indication of how seriously North Korea is taking its Olympic diplomatic mission.
Kim Jong Un's Olympic plans also include a massive military parade on Thursday through the streets of the North Korean capital Pyongyang. The display would be an attempt "to scare the hell out of the Americans," a diplomatic source told CNN last month."""


word_cnt_dict = {}


for word in news_str.split():
    word = word.lower()
    if word[0] in ["'", '"']:
        word = word[1:]
    if word[-1] in ["'", '"', ",", "."]:
        word = word[:-1]

    if not word_cnt_dict.get(word):
        word_cnt_dict[word] = 1
    else:
        word_cnt_dict[word] = word_cnt_dict[word] + 1


for word, cnt in word_cnt_dict.items():
    print(word, cnt)


















