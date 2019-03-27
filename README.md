# Code Louisville Python/SQL project.

In this project, I will try to answer the following question:

## Does the Federal Reserve take into account the Stock Market when making decisions on the Federal Funds Rate?

The Federal Reserve has repeatedly stated that it does not take into account stock prices when deliberating on rate action. I have obtained historical stock market , GDP growth, and federal funds rate(FFR) data and will attempt to establish if there is a relationship between them. Obviously the data will have some correlation - market conditions may reflect economic conditions, and as such, we will use GDP growth as a control. GDP growth might be the best indicator of economic conditions at a glance, this project will attempt to discern if the relationship between the FFR and the S&P 500 ever deviates from the relationship between the FFR and GDP growth in the United States, going back to 1954.

### Methods
In this project, I will be analyzing the data using the following methods:

- A Linear Regression between FFR and GDP, and FFR and S&P 500 (month over month % change).
- Linear regression between FFR and GDP, FFR and S&P 500 per fed chairman.
- Conditional probability of rate decrease given S&P 500 decrease.
- Conditional probability of rate decrease given S&P 500 decrease.

### Observations

Historically, both GDP and S&P 500 are very slightly negatively correlated with the FFR. However, this trend flipped with Alan Greenspan's tenure as fed chairman. Since Greenspan, the FFR and the S&P 500 have a slightly positive correlation. This probably has something to do with Greenspan's rapid reduction in rates after the .com bubble popped, followed by stock market recovery as Greenspan slowly raised rates over the next decade. Every successive fed chair has maintained this positive correlation, while the negative correlation between GDP and FFR remains intact. 

Probability of rate decrease month after S&P 500 decline - 0.408

Probability of rate decrease month after GDP decline - 0.667

The Federal Reserve is *much* more likely to cut rates after a GDP decline than a stock market decline.

Initially, this project asked the question- "does the relationship between the FFR and the S&P 500 ever deviate from the relationship between the FFR and GDP?" The answer is most definitely yes, and it is part of a trend that started 20 years ago. Although it might not be an intuitive relationship, the trend of the last 20 years is that the stock market and FFR are positively correlated.

To be frank, I am not sure that my observation or the manner in which I analyzed the data is meaningless or not.