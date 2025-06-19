# <ruby> 漢 <rp>(</rp><rt>hàn</rt><rp>)</rp>字 <rp>(</rp><rt>zì</rt><rp>)</rp></ruby>AI

 <ruby> 漢 <rp>(</rp><rt>hàn</rt><rp>)</rp>字 <rp>(</rp><rt>zì</rt><rp>)</rp></ruby>AI is a markov chain AI programmed in Python made to speak <ruby>
  中<rp>(</rp><rt>zhōng</rt><rp>)</rp>
  文<rp>(</rp><rt>wén</rt><rp>)</rp>
</ruby> (Chinese).

# dependencies
surprise there is non
# tools used
1. `pickle` - used as a save file state so the ai can learn more words the more you use it
2. `jieba` - used to tag the dataset used
3. `cc-cedict` - dataset used

# warning
the `markov_model.pkl` file can bloat up and slow down the computer if not deleted regularly.
# first words

> "***龙口市龙口夺食龙口龙胜县龙胜各族自治县龙利叶龙利龙人龙亭区龙亭龙井茶龙井市龙井区龙井龙齾龌龊龌浊龌腭裂***"

# interesting sentences made by the chain

> "*鲚鲿鳢鱼鳢鱥鳡鳣鲙鱼鲙鲎鱼*" (OLD)

![Screenshot 2025-05-12 7 53 28 PM](https://github.com/user-attachments/assets/f3db453a-f5a4-4b0b-954b-c83784a1584e)

> "*鬼名堂鬼叫鬼剃头*"
> "*老年期老少翻覆，翡冷翠?*"
## funny/cursed sentences
- > "*一把钥匙开一把锁，一把屎一把尿一心一德!*"
- > "*要命，要，西双版纳粗榧.*"
- > "*遵医嘱适温远隔千里？*"
- > "*见方要么要旨要强.*
- > "*顶面顶端顶岗*"




# credit
![88x31](https://github.com/user-attachments/assets/a36902ba-90c8-43e9-aac7-37d58d1dfb83)
![banner_320x60](https://github.com/user-attachments/assets/2ee07b62-c654-4b22-bb73-ff84dea3bff6)


# devlog
<details>
<summary><blockquote>add pos (date unknown)</blockquote> </summary>
<code>https://github.com/linuxfandudeguy/hanziai/blob/master/pos_structures.txt </code>
</details>
<details>
<summary><blockquote>add punc (2025-06-19T17:39:20.366Z)</blockquote> </summary>
<code>root in hanziai on  master [!?] via 🐍 v3.10.12
❯ python3 ai.py
2025-06-19 13:14:09,628 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:14:09,697 - DEBUG - Total entries loaded: 119624
2025-06-19 13:14:09,698 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:14:09,702 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:14:09,702 - DEBUG - Loaded 49 POS structures
2025-06-19 13:14:09,727 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:14:09,727 - DEBUG - Updating Markov Chain...
2025-06-19 13:14:09,729 - DEBUG - Markov chain now has 35964 states
2025-06-19 13:14:09,759 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:14:09,759 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;n&#39;, &#39;v&#39;, &#39;n&#39;, &#39;a&#39;]
POS structure: n v n a
Generated sentence with punctuation: 糖醇糊弄，精肉？

root in hanziai on  master [!?] via 🐍 v3.10.12
❯ python3 ai.py
2025-06-19 13:16:28,757 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:16:28,825 - DEBUG - Total entries loaded: 119624
2025-06-19 13:16:28,827 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:16:28,831 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:16:28,831 - DEBUG - Loaded 49 POS structures
2025-06-19 13:16:28,856 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:16:28,856 - DEBUG - Updating Markov Chain...
2025-06-19 13:16:28,858 - DEBUG - Markov chain now has 38961 states
2025-06-19 13:16:28,889 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:16:28,889 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;d&#39;, &#39;v&#39;, &#39;v&#39;, &#39;n&#39;]
POS structure: d v v n
Generated sentence with punctuation: 老来少翻转，翻沉？

root in hanziai on  master [!?] via 🐍 v3.10.12
❯ python3 ai.py
2025-06-19 13:16:33,572 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:16:33,640 - DEBUG - Total entries loaded: 119624
2025-06-19 13:16:33,643 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:16:33,646 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:16:33,646 - DEBUG - Loaded 49 POS structures
2025-06-19 13:16:33,673 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:16:33,673 - DEBUG - Updating Markov Chain...
2025-06-19 13:16:33,675 - DEBUG - Markov chain now has 41958 states
2025-06-19 13:16:33,709 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:16:33,709 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;n&#39;, &#39;u&#39;, &#39;v&#39;, &#39;n&#39;]
2025-06-19 13:16:33,721 - WARNING - No starting sequence matches the POS pattern start; picking random.
POS structure: n u v n
Generated sentence with punctuation: 干煸四季豆，乳头瘤乳臭未干乳糖？

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:17:45,716 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:17:45,784 - DEBUG - Total entries loaded: 119624
2025-06-19 13:17:45,786 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:17:45,790 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:17:45,790 - DEBUG - Loaded 49 POS structures
2025-06-19 13:17:45,818 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:17:45,818 - DEBUG - Updating Markov Chain...
2025-06-19 13:17:45,821 - DEBUG - Markov chain now has 44954 states
2025-06-19 13:17:45,855 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:17:45,855 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;v&#39;, &#39;r&#39;, &#39;v&#39;, &#39;n&#39;]
POS structure: v r v n
Generated sentence with punctuation: 佩服你作为，作数。

root in hanziai on  master [!?] via 🐍 v3.10.12
❯   python3 ai.py
2025-06-19 13:20:06,893 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:20:06,958 - DEBUG - Total entries loaded: 119624
2025-06-19 13:20:06,960 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:20:06,964 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:20:06,964 - DEBUG - Loaded 49 POS structures
2025-06-19 13:20:06,994 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:20:06,994 - DEBUG - Updating Markov Chain...
2025-06-19 13:20:06,996 - DEBUG - Markov chain now has 47951 states
2025-06-19 13:20:07,032 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:20:07,032 - DEBUG - Generating sentence of length 2 with POS pattern [&#39;n&#39;, &#39;a&#39;]
POS structure: n a
Generated sentence with punctuation: 一秘一睹！

root in hanziai on  master [!?] via 🐍 v3.10.12
❯ python3 ai.py
2025-06-19 13:21:02,525 - DEBUG - Loading data from hanziai_pos.mar
\2025-06-19 13:21:02,591 - DEBUG - Total entries loaded: 119624
2025-06-19 13:21:02,593 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:21:02,596 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:21:02,596 - DEBUG - Loaded 49 POS structures
2025-06-19 13:21:02,627 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:21:02,627 - DEBUG - Updating Markov Chain...
2025-06-19 13:21:02,629 - DEBUG - Markov chain now has 50948 states
2025-06-19 13:21:02,678 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:21:02,678 - DEBUG - Generating sentence of length 5 with POS pattern [&#39;n&#39;, &#39;v&#39;, &#39;c&#39;, &#39;n&#39;, &#39;v&#39;]
POS structure: n v c n v
Generated sentence with punctuation: 世运丕变且说！

root in hanziai on  master [!?] via 🐍 v3.10.12
❯ \python3 ai.py&#39;
∙ ^C

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:23:13,332 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:23:13,396 - DEBUG - Total entries loaded: 119624
2025-06-19 13:23:13,398 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:23:13,402 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:23:13,402 - DEBUG - Loaded 49 POS structures
2025-06-19 13:23:13,433 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:23:13,433 - DEBUG - Updating Markov Chain...
2025-06-19 13:23:13,442 - DEBUG - Markov chain now has 53944 states
2025-06-19 13:23:13,491 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:23:13,491 - DEBUG - Generating sentence of length 6 with POS pattern [&#39;r&#39;, &#39;v&#39;, &#39;n&#39;, &#39;c&#39;, &#39;v&#39;, &#39;n&#39;]
POS structure: r v n c v n
Generated sentence with punctuation: 你作为，作数。

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:24:50,853 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:24:50,917 - DEBUG - Total entries loaded: 119624
2025-06-19 13:24:50,919 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:24:50,923 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:24:50,923 - DEBUG - Loaded 49 POS structures
2025-06-19 13:24:50,965 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:24:50,965 - DEBUG - Updating Markov Chain...
2025-06-19 13:24:50,967 - DEBUG - Markov chain now has 56941 states
2025-06-19 13:24:51,018 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:24:51,018 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;a&#39;, &#39;c&#39;, &#39;a&#39;, &#39;n&#39;]
2025-06-19 13:24:51,034 - WARNING - No starting sequence matches the POS pattern start; picking random.
POS structure: a c a n
Generated sentence with punctuation: 新几内亚新官上任三把火斯蒂文！

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:27:58,276 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:27:58,343 - DEBUG - Total entries loaded: 119624
2025-06-19 13:27:58,345 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:27:58,349 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:27:58,349 - DEBUG - Loaded 49 POS structures
2025-06-19 13:27:58,389 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:27:58,389 - DEBUG - Updating Markov Chain...
2025-06-19 13:27:58,391 - DEBUG - Markov chain now has 59938 states
2025-06-19 13:27:58,442 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:27:58,442 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;v&#39;, &#39;r&#39;, &#39;v&#39;, &#39;n&#39;]
POS structure: v r v n
Generated sentence with punctuation: 佩服你作为，作数！

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:28:14,117 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:28:14,182 - DEBUG - Total entries loaded: 119624
2025-06-19 13:28:14,184 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:28:14,187 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:28:14,188 - DEBUG - Loaded 49 POS structures
2025-06-19 13:28:14,231 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:28:14,232 - DEBUG - Updating Markov Chain...
2025-06-19 13:28:14,234 - DEBUG - Markov chain now has 62935 states
2025-06-19 13:28:14,286 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:28:14,286 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;n&#39;, &#39;v&#39;, &#39;v&#39;, &#39;n&#39;]
POS structure: n v v n
Generated sentence with punctuation: 飞艇飘香，飘舞。

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:28:15,365 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:28:15,430 - DEBUG - Total entries loaded: 119624
2025-06-19 13:28:15,432 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:28:15,435 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:28:15,436 - DEBUG - Loaded 49 POS structures
2025-06-19 13:28:15,484 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:28:15,484 - DEBUG - Updating Markov Chain...
2025-06-19 13:28:15,486 - DEBUG - Markov chain now has 65931 states
2025-06-19 13:28:15,541 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:28:15,541 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;n&#39;, &#39;d&#39;, &#39;v&#39;, &#39;a&#39;]
POS structure: n d v a
Generated sentence with punctuation: 制裁到场删掉。

root in hanziai on  master [!?] via 🐍 v3.10.12
❯ python3 ai.py
2025-06-19 13:30:17,322 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:30:17,388 - DEBUG - Total entries loaded: 119624
2025-06-19 13:30:17,389 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:30:17,393 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:30:17,393 - DEBUG - Loaded 49 POS structures
2025-06-19 13:30:17,440 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:30:17,440 - DEBUG - Updating Markov Chain...
2025-06-19 13:30:17,442 - DEBUG - Markov chain now has 68927 states
2025-06-19 13:30:17,495 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:30:17,495 - DEBUG - Generating sentence of length 3 with POS pattern [&#39;r&#39;, &#39;v&#39;, &#39;n&#39;]
POS structure: r v n
Generated sentence with punctuation: 反正一样反射区治疗，反问语气！

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:30:59,470 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:30:59,535 - DEBUG - Total entries loaded: 119624
2025-06-19 13:30:59,537 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:30:59,541 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:30:59,541 - DEBUG - Loaded 49 POS structures
2025-06-19 13:30:59,589 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:30:59,589 - DEBUG - Updating Markov Chain...
2025-06-19 13:30:59,590 - DEBUG - Markov chain now has 71922 states
2025-06-19 13:30:59,645 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:30:59,645 - DEBUG - Generating sentence of length 5 with POS pattern [&#39;d&#39;, &#39;d&#39;, &#39;v&#39;, &#39;a&#39;, &#39;n&#39;]
POS structure: d d v a n
Generated sentence with punctuation: 逐次逐个逆袭！

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:32:28,445 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:32:28,508 - DEBUG - Total entries loaded: 119624
2025-06-19 13:32:28,510 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:32:28,513 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:32:28,514 - DEBUG - Loaded 49 POS structures
2025-06-19 13:32:28,561 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:32:28,561 - DEBUG - Updating Markov Chain...
2025-06-19 13:32:28,563 - DEBUG - Markov chain now has 74919 states
2025-06-19 13:32:28,619 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:32:28,619 - DEBUG - Generating sentence of length 4 with POS pattern [&#39;n&#39;, &#39;d&#39;, &#39;v&#39;, &#39;a&#39;]
POS structure: n d v a
Generated sentence with punctuation: 配方酌量酌酒？

root in hanziai on  master [!?] via 🐍 v3.10.12
❯  python3 ai.py
2025-06-19 13:33:24,965 - DEBUG - Loading data from hanziai_pos.mar
2025-06-19 13:33:25,029 - DEBUG - Total entries loaded: 119624
2025-06-19 13:33:25,031 - DEBUG - Sampled 3000 word-POS pairs for training
2025-06-19 13:33:25,035 - DEBUG - Loading structures from pos_structures.txt
2025-06-19 13:33:25,035 - DEBUG - Loaded 49 POS structures
2025-06-19 13:33:25,084 - DEBUG - Loaded existing Markov Chain model
2025-06-19 13:33:25,085 - DEBUG - Updating Markov Chain...
2025-06-19 13:33:25,086 - DEBUG - Markov chain now has 77915 states
2025-06-19 13:33:25,144 - DEBUG - Saved Markov Chain model to markov_model.pkl
2025-06-19 13:33:25,144 - DEBUG - Generating sentence of length 5 with POS pattern [&#39;d&#39;, &#39;v&#39;, &#39;n&#39;, &#39;c&#39;, &#39;n&#39;]
POS structure: d v n c n
Generated sentence with punctuation: 相声相聚，相片！ </code>
</details>

