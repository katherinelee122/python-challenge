{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv((\"budget_data.csv\"),encoding = \"utf-8\",sep =\",\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-10</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-10</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-10</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-10</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-10</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses\n",
       "0  Jan-10         867884\n",
       "1  Feb-10         984655\n",
       "2  Mar-10         322013\n",
       "3  Apr-10         -69417\n",
       "4  May-10         310503"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TP: 38382578\n",
      "85\n",
      "671099\n",
      "PC: 671099\n",
      "PP: 671099\n",
      "RC: [671099]\n",
      "GI: 0\n",
      "GD: 9999999999999999\n",
      "RA: 1.0\n"
     ]
    }
   ],
   "source": [
    "total_months = 0\n",
    "total_profit = 0\n",
    "prev_profit = 0\n",
    "profit_change = 0\n",
    "greatest_increase = 0\n",
    "greatest_decrease = 9999999999999999\n",
    "rev_change=[]\n",
    "for i in range(len(df)):\n",
    "    total_months = total_months + 1\n",
    "# total_profit = total_profit + int(row([1]))\n",
    "total_profit = df[\"Profit/Losses\"].sum()\n",
    "print(\"TP: {}\".format(total_profit))\n",
    "print(i)\n",
    "print(df.iloc[i,1])\n",
    "profit_change = df.iloc[i,1] - prev_profit\n",
    "print(\"PC: {}\".format(profit_change))\n",
    "prev_profit = df.iloc[i,1]\n",
    "print(\"PP: {}\".format(prev_profit))\n",
    "if(profit_change == df.iloc[i,1]):\n",
    "    profit_change=0\n",
    "rev_change.append(df.iloc[i,1])\n",
    "print(\"RC: {}\".format(rev_change))\n",
    "    #rev_change.append(int(row[1]))\n",
    "if(profit_change > greatest_increase == df.iloc[i,1]):\n",
    "    greatest_increase[1] = profit_change\n",
    "    greatest_increase[0] = row[0]\n",
    "print(\"GI: {}\".format(greatest_increase))\n",
    "if(profit_change < greatest_decrease == df.iloc[i,1]):\n",
    "    greatest_decrease[1] = profit_change\n",
    "    greatest_decrease[0] = row[0]\n",
    "print(\"GD: {}\".format(greatest_decrease))\n",
    "#  print(profit_change)\n",
    "revenue_avg = sum(rev_change) / df.iloc[i,1]\n",
    "print(\"RA: {}\".format(revenue_avg))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-25-9ee72c32f94c>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-25-9ee72c32f94c>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    f.write(\"profit change:\"+ str(round(profit_change,2)) + \"\\n\")\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "f = open (\"result.txt\",\"w\")\n",
    "f.write(\"Analysis\\n\")\n",
    "f.write(\"---------------\\n\")\n",
    "f.write((\"total months:\" +str(total_months)) + \"\\n\",\n",
    "f.write(\"total profit:\" + str(total_profit) + \"\\n\"\n",
    "f.write(\"profit change:\"+ str(round(profit_change,2)) + \"\\n\")\n",
    "f.write(\"greatest increase:\" + str(greatest_increase) + \"\\n\"\n",
    "f.write(\"greatest decrease:\" + str(greatest_decrease) + \")\\n\"\n",
    "f.close()\n",
    "print(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
