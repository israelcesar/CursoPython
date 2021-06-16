{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d5910c11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 abacate R$ 2,00\n",
      "2 bola R$ 5,00\n",
      "3 cachorro Não tem preço\n",
      "4 dinheiro Não tem preço\n",
      "5 elefante Não tem preço\n"
     ]
    }
   ],
   "source": [
    "# zip\n",
    "\n",
    "lista1 = [1, 2, 3, 4, 5]\n",
    "lista2 = [\"abacate\", \"bola\", \"cachorro\", \"dinheiro\", \"elefante\"]\n",
    "lista3 = [\"R$ 2,00\", \"R$ 5,00\", \"Não tem preço\", \"Não tem preço\", \"Não tem preço\"]\n",
    "\n",
    "for numero, nome, preco in zip(lista1, lista2, lista3):\n",
    "    print (numero, nome, preco)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62109faa",
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
