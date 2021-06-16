{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0e5bd1d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "41\n"
     ]
    }
   ],
   "source": [
    "# Função reduce\n",
    "\n",
    "from functools import reduce\n",
    "\n",
    "def soma(x, y):\n",
    "    return x+y\n",
    "\n",
    "lista = [1, 3, 5, 10, 20]\n",
    "\n",
    "soma = reduce(soma, lista)\n",
    "print (soma)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc2015df",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
