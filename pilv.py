from wordcloud import WordCloud 
pilv=WordCloud() .generate(open("aisakell.txt", "r") .read())
pilt=pilv.to_image()
pilt.save("pilt1.png")