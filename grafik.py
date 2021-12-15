{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-9ee99fb6431f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0mi\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;36m10\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0mi\u001b[0m\u001b[0;34m+=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m     \u001b[0mc\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Öğrencinin ismini giriniz\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m     \u001b[0ma\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0md\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Öğrencinin boyunu giriniz (cm)\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: 'str' object is not callable"
     ]
    }
   ],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "a=[]\n",
    "b=[]\n",
    "f=[]\n",
    "i=0\n",
    "\n",
    "while i != 10:\n",
    "    i+=1\n",
    "    c=input(\"Öğrencinin ismini giriniz\")\n",
    "    a.append(c)\n",
    "    d=int(input(\"Öğrencinin boyunu giriniz (cm)\"))\n",
    "    b.append(d)\n",
    "    d=int(input(\"Öğrencinin kilosunu giriniz (kg)\"))\n",
    "    f.append(d)\n",
    "\n",
    "plt.bar(a,b)\n",
    "plt.legend()\n",
    "plt.xlabel(\" \")\n",
    "plt.ylabel(\"Boy (cm)\")\n",
    "plt.title(\"Boy\")\n",
    "plt.show()\n",
    "\n",
    "plt.bar(a,f)\n",
    "plt.legend()\n",
    "plt.xlabel(\" \")\n",
    "plt.ylabel(\"Kilo (kg)\")\n",
    "plt.title(\"Kilo\")\n",
    "plt.show()"
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
  "interpreter": {
   "hash": "916dbcbb3f70747c44a77c7bcd40155683ae19c65e1c03b4aa3499c5328201f1"
  },
  "kernelspec": {
   "display_name": "Python 3.8.10 64-bit",
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
   "version": "3.8.10"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
