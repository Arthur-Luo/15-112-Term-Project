from cmu_112_graphics import *
from PIL import ImageTk, Image
import random, math, copy

################################################################################
# classes
################################################################################

class Card(object):
    def __init__(self, cardNum):
        self.cardNum = cardNum
        self.front = PtSide(cardNum)
        self.back = VegSide(cardNum)
        neededVegList = [
                ['lettuce'],
                ['lettuce','carrot'],
                ['lettuce'],
                ['lettuce'],
                ['lettuce','onion'],
                ['pepper','lettuce','cabbage'],
                ['cabbage','onion'],
                ['pepper','tomato'],
                ['pepper'],
                ['pepper','onion'],
                ['pepper'],
                ['pepper','onion','cabbage'],
                ['onion','carrot'],
                ['carrot','lettuce'],
                ['onion'],
                ['onion'],
                ['cabbage','pepper'],
                ['carrot','onion','pepper'],
                ['cabbage'],
                ['cabbage','lettuce'],
                ['onion','pepper'],
                ['pepper','cabbage','tomato'],
                ['cabbage'],
                ['cabbage','lettuce'],
                ['carrot','pepper'],
                ['lettuce','carrot','onion'],
                ['tomato','pepper'],
                ['carrot'],
                ['carrot','lettuce'],
                ['lettuce','onion'],
                ['tomato'],
                ['tomato','lettuce'],
                ['tomato'],
                ['tomato'],
                ['tomato'],
                ['cabbage','lettuce']
                ]
        self.neededVeg = neededVegList[self.cardNum]

    def flip(self):
        # flip the card
        self.front = self.back
        self.back = self.front

    def score(self, hand):
        # return the score of the ptCard given a hand
        if isinstance(self.front, PtSide):
            return self.front.score(hand)

    def __repr__(self):
        # for debugging we want to print the card number
        return f'Card {self.cardNum}'
    
    def drawOnCanvas(self, app, canvas, cx, cy):
        # draw the front side of the card
        if isinstance(self.front, VegSide):
            if self.front.veg == 'pepper':
                img = app.pepperImg
            elif self.front.veg == 'lettuce':
                img = app.lettuceImg
            elif self.front.veg == 'tomato':
                img = app.tomatoImg
            elif self.front.veg == 'carrot':
                img = app.carrotImg
            elif self.front.veg == 'cabbage':
                img = app.cabbageImg
            else:
                img = app.onionImg
            canvas.create_image(cx, cy, pilImage=img)
        else:
            img = app.ptSideImgs[self.cardNum]
            canvas.create_image(cx, cy, pilImage=img)

    def drawSmallOnCanvas(self, app, canvas, cx, cy):
        # draw a smaller version in player areas
        if isinstance(self.front, VegSide):
            if self.front.veg == 'pepper':
                img = app.smallPepperImg
            elif self.front.veg == 'lettuce':
                img = app.smallLettuceImg
            elif self.front.veg == 'tomato':
                img = app.smallTomatoImg
            elif self.front.veg == 'carrot':
                img = app.smallCarrotImg
            elif self.front.veg == 'cabbage':
                img = app.smallCabbageImg
            else:
                img = app.smallOnionImg
            canvas.create_image(cx, cy, pilImage=img)
        else:
            img = app.smallPtSideImgs[self.cardNum]
            canvas.create_image(cx, cy, pilImage=img)

    
class PtSide(object):
    def __init__(self, cardNum):
        self.cardNum = cardNum

    def score(self, hand):
        # return the score of the ptCard given a hand
        score = 0
        # a dict would be more elegant but we can't store a scoring criteria in 
        # a dict and even if we can we would still have to build the dict up
        # one by one as every card is different
        if self.cardNum == 0:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card == 'lettuce':
                        score += 2
            return score
        elif self.cardNum == 1:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'lettuce':
                        score += 2
                    if card.front.veg == 'carrot':
                        score += 2
                    if card.front.veg == 'onion':
                        score -= 4
            return score
        elif self.cardNum == 2:
            for card in hand:
                lettuceCount = 0
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'lettuce':
                        lettuceCount += 1
            return (lettuceCount // 3) * 8
        elif self.cardNum == 3:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'lettuce':
                        score += 3
                    if card.front.veg == 'carrot':
                        score -= 2
            return score
        elif self.cardNum == 4:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'lettuce':
                        score += 1
                    if card.front.veg == 'onion':
                        score += 1
            return score
        elif self.cardNum == 5:
            pepperCount = 0
            lettuceCount = 0
            cabbageCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'pepper':
                        pepperCount += 1
                    if card.front.veg == 'lettuce':
                        lettuceCount += 1
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
            return min(pepperCount, lettuceCount, cabbageCount) * 8
        elif self.cardNum == 6:
            cabbageCount = 0
            onionCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
                    if card.front.veg == 'onion':
                        onionCount += 1
            return min(cabbageCount, onionCount) * 5
        elif self.cardNum == 7:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'pepper':
                        score += 2
                    if card.front.veg == 'tomato':
                        score += 1
                    if card.front.veg == 'lettuce':
                        score -= 2
            return score
        elif self.cardNum == 8:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'pepper':
                        score += 4
                    if card.front.veg == 'onion':
                        score -= 2
                    if card.front.veg == 'carrot':
                        score -= 2
            return score
        elif self.cardNum == 9:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'pepper':
                        score += 1
                    if card.front.veg == 'onion':
                        score += 1
            return score
        elif self.cardNum == 10:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'pepper':
                        score += 3
                    if card.front.veg == 'tomato':
                        score -= 1
                    if card.front.veg == 'lettuce':
                        score -= 1
            return score
        elif self.cardNum == 11:
            onionCount = 0
            pepperCount = 0
            cabbageCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'onion':
                        onionCount += 1
                    if card.front.veg == 'pepper':
                        pepperCount += 1
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
            return min(onionCount, pepperCount, cabbageCount) * 8
        elif self.cardNum == 12:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'onion':
                        score += 1
                    if card.front.veg == 'carrot':
                        score += 1
            return score
        elif self.cardNum == 13:
            carrotCount = 0
            lettuceCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'carrot':
                        carrotCount += 1
                    if card.front.veg == 'lettuce':
                        lettuceCount += 1
            return min(carrotCount, lettuceCount) * 5
        elif self.cardNum == 14:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'onion':
                        score += 4
                    if card.front.veg == 'carrot':
                        score -= 2
                    if card.front.veg == 'lettuce':
                        score -= 2
            return score
        elif self.cardNum == 15:
            onionCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'onion':
                        onionCount += 1
            return (onionCount // 3) * 8
        elif self.cardNum == 16:
            cabbageCount = 0
            pepperCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
                    if card.front.veg == 'pepper':
                        pepperCount += 1
            return min(cabbageCount, pepperCount) * 5
        elif self.cardNum == 17:
            carrotCount = 0
            onionCount = 0
            pepperCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'carrot':
                        carrotCount += 1
                    if card.front.veg == 'onion':
                        onionCount += 1
                    if card.front.veg == 'pepper':
                        pepperCount += 1
            return min(carrotCount, onionCount, pepperCount) * 8
        elif self.cardNum == 18:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        score += 3
                    if card.front.veg == 'lettuce':
                        score -= 1
                    if card.front.veg == 'carrot':
                        score -= 1
            return score 
        elif self.cardNum == 19:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        score += 1
                    if card.front.veg == 'lettuce':
                        score += 1
            return score
        elif self.cardNum == 20:
            onionCount = 0
            pepperCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'onion':
                        onionCount += 1
                    if card.front.veg == 'pepper':
                        pepperCount += 1    
            return min(onionCount, pepperCount) * 5
        elif self.cardNum == 21:
            pepperCount = 0
            cabbageCount = 0
            tomatoCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'pepper':
                        pepperCount += 1
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
                    if card.front.veg == 'tomato':
                        tomatoCount += 1
            return min(pepperCount, cabbageCount, tomatoCount) * 8
        elif self.cardNum == 22:
            cabbageCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
            return (cabbageCount // 2) * 5
        elif self.cardNum == 23:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        score += 2
                    if card.front.veg == 'lettuce':
                        score += 1
                    if card.front.veg == 'carrot':
                        score -= 2
            return score
        elif self.cardNum == 24:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'carrot':
                        score += 2
                    if card.front.veg == 'pepper':
                        score += 1
                    if card.front.veg == 'cabbage':
                        score -= 2
            return score
        elif self.cardNum == 25:
            lettuceCount = 0
            carrotCount = 0
            onionCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'lettuce':
                        lettuceCount += 1
                    if card.front.veg == 'carrot':
                        carrotCount += 1
                    if card.front.veg == 'onion':
                        onionCount += 1
            return min(lettuceCount, carrotCount, onionCount) * 8 
        elif self.cardNum == 26:
            tomatoCount = 0
            pepperCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'tomato':
                        tomatoCount += 1
                    if card.front.veg == 'pepper':
                        pepperCount += 1
            return min(tomatoCount, pepperCount) * 5
        elif self.cardNum == 27:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'carrot':
                        score += 2
            return score
        elif self.cardNum == 28:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'carrot':
                        score += 1
                    if card.front.veg == 'lettuce':
                        score += 1
            return score
        elif self.cardNum == 29:
            lettuceCount = 0
            onionCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'lettuce':
                        lettuceCount += 1
                    if card.front.veg == 'onion':
                        onionCount += 1
            return min(lettuceCount, onionCount) * 5
        elif self.cardNum == 30:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'tomato':
                        score += 4
                    if card.front.veg == 'cabbage':
                        score -= 2
                    if card.front.veg == 'pepper':
                        score -= 2
            return score
        elif self.cardNum == 31:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'tomato':
                        score += 2
                    if card.front.veg == 'lettuce':
                        score += 2
                    if card.front.veg == 'carrot':
                        score -= 4
            return score
        elif self.cardNum == 32:
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'tomato':
                        score += 3
                    if card.front.veg == 'carrot':
                        score -= 1
                    if card.front.veg == 'onion':
                        score -= 1
            return score
        elif self.cardNum == 33:
            tomatoCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'tomato':
                        tomatoCount += 1
            return (tomatoCount // 2) * 5
        elif self.cardNum == 34:
            tomatoCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'tomato':
                        tomatoCount += 1
            return (tomatoCount // 3) * 8
        elif self.cardNum == 35:
            cabbageCount = 0
            lettuceCount = 0
            for card in hand:
                if isinstance(card.front, VegSide):
                    if card.front.veg == 'cabbage':
                        cabbageCount += 1
                    if card.front.veg == 'lettuce':
                        lettuceCount += 1
            return min(cabbageCount, lettuceCount) * 5

class VegSide(object):
    def __init__(self, cardNum): 
        self.cardNum = cardNum
        vegList = ['pepper' for i in range(6)] +\
                  ['lettuce' for i in range(6)] +\
                  ['tomato' for i in range(6)] +\
                  ['carrot' for i in range(6)] +\
                  ['cabbage' for i in range(6)] +\
                  ['onion' for i in range(6)]
        self.veg = vegList[self.cardNum]

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        # initialize the deck
        for i in range(36):
            self.cards.append(Card(i))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)
    
    def split2Piles(self):
        # split to 3 piles
        piles = {}
        for pileNum in range(3):
            piles[pileNum] = Pile(pileNum, self.cards)
        return piles

class Pile(object):
    def __init__(self, pileNum, deck):
        self.pileNum = pileNum
        self.cards = deck[self.pileNum*12:(self.pileNum+1)*12]

    def drawOnCanvas(self, app, canvas):
        # draw the top card on canvas
        if self.cards != []:
            cx1 = app.width / 8
            cx2 = app.width / 4
            cx3 = app.width * 3/8
            cy = app.height / 4
            if self.pileNum == 0:
                self.cards[-1].drawOnCanvas(app, canvas, cx1, cy)
            elif self.pileNum == 1:
                self.cards[-1].drawOnCanvas(app, canvas, cx2, cy)
            elif self.pileNum == 2:
                self.cards[-1].drawOnCanvas(app, canvas, cx3, cy)

class VegMkt(object):
    def __init__(self):
        self.cards = {}
    
    def build(self, deck):
        # initialize the veggie market
        for vegNum in range(6):
            self.cards[vegNum] = deck.cards.pop()
            self.cards[vegNum].flip()

    def drawFromPile(self, piles, vegNum):
        # refill a card from the corresponding pile
        pileNum = vegNum // 2
        if piles[pileNum].cards != []:
            self.cards[vegNum] = piles[pileNum].cards.pop()
            if self.cards[vegNum] != None:
                self.cards[vegNum].flip()
    
    def drawCardsOnCanvas(self, app, canvas):
        # draw the six cards in the market
        cx1 = app.width / 8
        cx2 = app.width / 4
        cx3 = app.width * 3/8
        cy1 = app.height / 2
        cy2 = app.height * 3/4
        if self.cards[0] != None:
            self.cards[0].drawOnCanvas(app, canvas, cx1, cy1)
        if self.cards[1] != None:
            self.cards[1].drawOnCanvas(app, canvas, cx1, cy2)
        if self.cards[2] != None:
            self.cards[2].drawOnCanvas(app, canvas, cx2, cy1)
        if self.cards[3] != None:
            self.cards[3].drawOnCanvas(app, canvas, cx2, cy2)
        if self.cards[4] != None:
            self.cards[4].drawOnCanvas(app, canvas, cx3, cy1)
        if self.cards[5] != None:
            self.cards[5].drawOnCanvas(app, canvas, cx3, cy2)
    
    def drawVegMktArea(self, app, canvas):
        # draw the veggie market area
        x0 = 0
        y0 = app.height * 3/8
        x1 = app.width / 2
        y1 = app.height
        canvas.create_rectangle(x0, y0, x1, y1, fill='')
        canvas.create_text(x0+5, y0+5, anchor=NW, text='Veggie \nMarket',
        font='Arial 18')

class Player(object):
    def __init__(self, playerNum):
        self.playerNum = playerNum
        self.hand = []
    
    def getScore(self):
        # return the total score of the player
        score = 1
        for card in self.hand:
            if isinstance(card.front, PtSide):
                score += card.front.score(self.hand)
        return score
    
    def isPlayersTurn(self, app):
        # determine if it is currently the player's turn to draft
        if self.playerNum == 1:
            if app.counter % 2 == 0:
                return True
            return False
        if app.counter % 2 == 1:
            return True
        return False
    
    def optionalFlip(self, app, event):
        # handles the optional movement to flip a point card
        ptCards = []
        width = app.smallCardWidth
        height = app.smallCardHeight
        if self.playerNum == 1:
            cy = app.height / 6
        else:
            cy = app.height * 2/3
        for card in self.hand:
            if isinstance(card.front, PtSide):
                ptCards.append(card)
        for i in range(len(ptCards)): 
            cx = app.width/2 + ((i+1)/(len(ptCards)+1)) * app.width/2
            if (cx-width/2 <= event.x <= cx+width/2 
            and cy-height/2 <= event.y <= cy+height/2):
                ptCards[i].flip()
                app.counter += 1
                break

    def drawFromPile(self, pile):
        # draft a card from a pile
        if pile.cards != []:
            self.hand.append(pile.cards.pop())
    
    def drawFromVegMkt(self, vegMkt, vegNum):
        # draft a card from the veggie market
        if vegMkt.cards[vegNum] != None:
            self.hand.append(vegMkt.cards[vegNum])
            vegMkt.cards[vegNum] = None

    def drawCardsOnCanvas(self, app, canvas):
        # draw the player's hand
        ptCards = []
        pepperCount = 0
        lettuceCount = 0
        tomatoCount = 0
        carrotCount = 0
        cabbageCount = 0
        onionCount = 0
        for card in self.hand:
            if isinstance(card.front, PtSide):
                ptCards.append(card)
            elif card.front.veg == 'pepper':
                pepperCount += 1
            elif card.front.veg == 'lettuce':
                lettuceCount += 1
            elif card.front.veg == 'tomato':
                tomatoCount += 1
            elif card.front.veg == 'carrot':
                carrotCount += 1
            elif card.front.veg == 'cabbage':
                cabbageCount += 1
            else:
                onionCount += 1
        cx1 = app.width - app.width * 6/14 
        cx2 = app.width - app.width * 5/14 
        cx3 = app.width - app.width * 4/14 
        cx4 = app.width - app.width * 3/14 
        cx5 = app.width - app.width * 2/14 
        cx6 = app.width - app.width / 14
        if self.playerNum == 1:
            cy1 = app.height / 6
            if ptCards != []:
                for i in range(len(ptCards)): # draw the ptCards
                    cx = app.width/2 + ((i+1)/(len(ptCards)+1)) * app.width/2
                    ptCards[i].drawSmallOnCanvas(app, canvas, cx, cy1)
            cy2 = app.height / 3
            # draw the veggies and their counts
            if pepperCount != 0:
                canvas.create_image(cx1, cy2, pilImage=app.smallPepperImg)
                canvas.create_text(cx1, cy2, text=f'x{pepperCount}'
                , font='Arial 16 bold', fill='white')
            if lettuceCount != 0:
                canvas.create_image(cx2, cy2, pilImage=app.smallLettuceImg)
                canvas.create_text(cx2, cy2, text=f'x{lettuceCount}'
                , font='Arial 16 bold', fill='white')
            if tomatoCount != 0:
                canvas.create_image(cx3, cy2, pilImage=app.smallTomatoImg)
                canvas.create_text(cx3, cy2, text=f'x{tomatoCount}'
                , font='Arial 16 bold', fill='white')
            if carrotCount != 0:
                canvas.create_image(cx4, cy2, pilImage=app.smallCarrotImg)
                canvas.create_text(cx4, cy2, text=f'x{carrotCount}'
                , font='Arial 16 bold', fill='white')
            if cabbageCount != 0:
                canvas.create_image(cx5, cy2, pilImage=app.smallCabbageImg)
                canvas.create_text(cx5, cy2, text=f'x{cabbageCount}'
                , font='Arial 16 bold', fill='white')
            if onionCount != 0:
                canvas.create_image(cx6, cy2, pilImage=app.smallOnionImg)
                canvas.create_text(cx6, cy2, text=f'x{onionCount}'
                , font='Arial 16 bold', fill='white')
        if self.playerNum == 2:
            cy1 = app.height * 2/3
            if ptCards != []:
                for i in range(len(ptCards)): # draw the ptCards
                    cx = app.width/2 + ((i+1)/(len(ptCards)+1)) * app.width/2
                    ptCards[i].drawSmallOnCanvas(app, canvas, cx, cy1)
            cy2 = app.height * 5/6
            # draw the veggies and their counts
            if pepperCount != 0:
                canvas.create_image(cx1, cy2, pilImage=app.smallPepperImg)
                canvas.create_text(cx1, cy2, text=f'x{pepperCount}'
                , font='Arial 16 bold', fill='white')
            if lettuceCount != 0:
                canvas.create_image(cx2, cy2, pilImage=app.smallLettuceImg)
                canvas.create_text(cx2, cy2, text=f'x{lettuceCount}'
                , font='Arial 16 bold', fill='white')
            if tomatoCount != 0:
                canvas.create_image(cx3, cy2, pilImage=app.smallTomatoImg)
                canvas.create_text(cx3, cy2, text=f'x{tomatoCount}'
                , font='Arial 16 bold', fill='white')
            if carrotCount != 0:
                canvas.create_image(cx4, cy2, pilImage=app.smallCarrotImg)
                canvas.create_text(cx4, cy2, text=f'x{carrotCount}'
                , font='Arial 16 bold', fill='white')
            if cabbageCount != 0:
                canvas.create_image(cx5, cy2, pilImage=app.smallCabbageImg)
                canvas.create_text(cx5, cy2, text=f'x{cabbageCount}'
                , font='Arial 16 bold', fill='white')
            if onionCount != 0:
                canvas.create_image(cx6, cy2, pilImage=app.smallOnionImg)
                canvas.create_text(cx6, cy2, text=f'x{onionCount}'
                , font='Arial 16 bold', fill='white')

    def drawPlayerArea(self, app, canvas):
        # draw the player's area boundaries
        if self.playerNum == 1:
            x0 = app.width / 2
            y0 = 0
            x1 = app.width
            y1 = app.height / 2
            cx = app.width * 3/4
            cy = app.height / 12
        else:
            x0 = app.width / 2
            y0 = app.height / 2
            x1 = app.width
            y1 = app.height
            cx = app.width * 3/4
            cy = app.height * 7/12
        canvas.create_rectangle(x0, y0, x1, y1, fill='')
        canvas.create_text(x0+5, y0+5, anchor=NW, 
        text=f'Player {self.playerNum}', font='Arial 18')
        canvas.create_text(cx, cy, anchor=S, 
            text='You can also click on one of your point cards '\
            'to flip it instead of drawing cards.', font='Arial 12')

    def drawHighLight(self, app, canvas):
        # draw the highlight around the player area if it is his/her turn
        if self.isPlayersTurn(app):
            if self.playerNum == 1:
                x0 = app.width / 2
                y0 = 0
                x1 = app.width
                y1 = app.height / 2
            else:
                x0 = app.width / 2
                y0 = app.height / 2
                x1 = app.width
                y1 = app.height
            canvas.create_rectangle(x0, y0, x1, y1, width=5, outline='red')
            canvas.create_text(x0+5, y0+28, anchor=NW, text='Current Player',
            font='Arial 18', fill='red')

class BotPlayer(Player):
    def autoPilot(self, app):
        # handle the bot's movement
        if self.isPlayersTurn(app):
            if arePilesEmpty(app):
                action = 'veg'
            else:
                action = random.choice(('pt', 'veg'))
            if action == 'pt':
                pileNum = random.randrange(3)
                while app.piles[pileNum] == None:
                    # make sure that the bot is drawing from a non-empty pile
                    pileNum = random.randrange(3)
                if app.isVegClickedPrev == False:
                    self.drawFromPile(app.piles[pileNum])
                    app.counter += 1
            else:
                vegNum = random.randrange(6)
                while app.vegMkt.cards[vegNum] == None:
                    # make sure the bot is drawing a non-empty veggie card
                    vegNum = random.randrange(6)
                app.isVegClickedPrev = not app.isVegClickedPrev
                self.drawFromVegMkt(app.vegMkt, vegNum)
                app.vegMkt.drawFromPile(app.piles, vegNum)
                if app.isVegClickedPrev:
                    # account for 2 veggies in a row
                    app.counter += 2
                else:
                    app.counter += 1
            if ifGameOver(app.vegMkt):
                app.gameOver = True
    
    def getHighestCountVeg(self):
        neededVeg = []
        for card in self.hand:
            if isinstance(card.front, PtSide):
                veg = card.neededVeg
                neededVeg.extend(veg)
        dict = {}
        dict['pepper'] = neededVeg.count('pepper')
        dict['lettuce'] = neededVeg.count('lettuce')
        dict['tomato'] = neededVeg.count('tomato')
        dict['carrot'] = neededVeg.count('carrot')
        dict['cabbage'] = neededVeg.count('cabbage')
        dict['onion'] = neededVeg.count('onion')
        dict = sorted(dict)
        result = []
        for key in dict:
            result.append(key)
        return result

    def normalAutoPilot(self, app):
        if self.isPlayersTurn(app):
            if arePilesEmpty(app):
                action = 'veg'
            elif self.hand == []:
                action = 'pt'
            else:
                action = random.choice(('pt', 'veg'))
            if action == 'pt':
                if action == 'pt':
                    pileNum = random.randrange(3)
                    while app.piles[pileNum] == None:
                        # make sure that the bot is drawing from a non-empty pile
                        pileNum = random.randrange(3)
                    if app.isVegClickedPrev == False:
                        self.drawFromPile(app.piles[pileNum])
                        app.counter += 1
            # if action = veg, then the normal bot should take the veggie that  
            # most needed according to the point cards in its hand. Compiling 
            # a list of veggies needed for each point card an implement a fn 
            # that returns the most needed veggie.
            if action == 'veg':
                vegList = self.getHighestCountVeg()
                vegNum = None
                for i in range(6):
                    for j in range(len(vegList)):
                        if (app.vegMkt.cards[i] != None and 
                        app.vegMkt.cards[i].front.veg == vegList[j]):
                            vegNum = i
                            break
                app.isVegClickedPrev = not app.isVegClickedPrev
                self.drawFromVegMkt(app.vegMkt, vegNum)
                app.vegMkt.drawFromPile(app.piles, vegNum)
                if app.isVegClickedPrev:
                    # account for 2 veggies in a row
                    app.counter += 2
                else:
                    app.counter += 1
            if ifGameOver(app.vegMkt):
                app.gameOver = True
        
    def hardAutoPilot(self, app):
        if self.isPlayersTurn(app):
            depth = app.depth
            currentEval = minimax(app.piles, app.vegMkt, app.player1, app.player2, depth, 2)
            for pileNum in range(3):
                piles = copy.deepcopy(app.piles)
                vegMkt = copy.deepcopy(app.vegMkt)
                player1 = copy.deepcopy(app.player1)
                player2 = copy.deepcopy(app.player2)
                player2.drawFromPile(piles[pileNum])
                evl = minimax(piles, vegMkt, player1, player2, depth-1, 1)
                print(f'evl: {evl} current evl: {currentEval}')
                if evl == currentEval:
                    self.drawFromPile(app.piles[pileNum])
                    app.counter += 1
                    return
            for i in range(6):
                for j in range(6):
                    piles = copy.deepcopy(app.piles)
                    vegMkt = copy.deepcopy(app.vegMkt)
                    player1 = copy.deepcopy(app.player1)
                    player2 = copy.deepcopy(app.player2)
                    player2.drawFromVegMkt(vegMkt, i)
                    vegMkt.drawFromPile(piles, i)
                    player2.drawFromVegMkt(vegMkt, j)
                    vegMkt.drawFromPile(piles, j)
                    evl = minimax(piles, vegMkt, player1, player2, depth-1, 1)
                    print(f'evl: {evl} current evl: {currentEval}')
                    if evl == currentEval:
                        self.drawFromVegMkt(app.vegMkt, i)
                        app.vegMkt.drawFromPile(app.piles, i)
                        self.drawFromVegMkt(app.vegMkt, j)
                        app.vegMkt.drawFromPile(app.piles, j)
                        app.counter += 1
                        if ifGameOver(app.vegMkt):
                            app.gameOver = True
                        return

    def dynamicAutoPilot(self, app):
        if heuristic(app.player1, app.player2) < -10:
            self.autoPilot(app)
        elif -10 <= heuristic(app.player1, app.player2) <= 10:
            self.normalAutoPilot(app)
        else:
            self.hardAutoPilot(app)      
    
################################################################################
# main function
################################################################################

def appStarted(app):
    app.cardWidth = 145
    app.cardHeight = 205
    app.smallCardWidth = 92
    app.smallCardHeight = 128
    # app.deck = [Card(i) for i in range(36)]
    app.deck = Deck()
    app.deck.shuffle()
    # random.shuffle(app.deck)
    app.vegMkt = VegMkt()
    app.vegMkt.build(app.deck)
    app.piles = app.deck.split2Piles()
    app.player1 = Player(1)
    app.player2 = Player(2)
    app.counter = 0
    app.isVegClickedPrev = False
    app.gameOver = False
    app.isStarted = False
    app.inBotMode = False
    app.inNormalBotMode = False
    app.inHardBotMode = False
    app.inDynamicBotMode = False
    app.depth = 2
    app.ptSideImgs = [getPtSideImg(app, cardNum) 
                      for cardNum in range(36)]
    app.smallPtSideImgs = [getSmallPtSideImg(app, cardNum) # small imgs to be
                           for cardNum in range(36)] # used in player areas
    app.lettuceImg = Image.open('Lettuce_cards-1-small.png')
    app.pepperImg = Image.open('Pepper_cards-1-small.png')
    app.carrotImg = Image.open('Carrot_cards-1-small.png')
    app.tomatoImg = Image.open('Tomato_cards-1-small.png')
    app.cabbageImg = Image.open('Cabbage_cards-1-small.png')
    app.onionImg = Image.open('Onion_cards-1-small.png')
    app.lettuceImg = app.scaleImage(app.lettuceImg, 0.8)
    app.pepperImg = app.scaleImage(app.pepperImg, 0.8)
    app.carrotImg = app.scaleImage(app.carrotImg, 0.8)
    app.tomatoImg = app.scaleImage(app.tomatoImg, 0.8)
    app.cabbageImg = app.scaleImage(app.cabbageImg, 0.8)
    app.onionImg = app.scaleImage(app.onionImg, 0.8)
    app.smallLettuceImg = app.scaleImage(app.lettuceImg, 0.625) # small imgs to
    app.smallPepperImg = app.scaleImage(app.pepperImg, 0.625) # be used in 
    app.smallCarrotImg = app.scaleImage(app.carrotImg, 0.625) # player areas
    app.smallTomatoImg = app.scaleImage(app.tomatoImg, 0.625) #
    app.smallCabbageImg = app.scaleImage(app.cabbageImg, 0.625) #
    app.smallOnionImg = app.scaleImage(app.onionImg, 0.625) #

def getPtSideImg(app, cardNum):
    return app.scaleImage(Image.open(f'{cardNum}.jpg'), 0.8)

def getSmallPtSideImg(app, cardNum):
    # return small imgs to be used in player areas
    return app.scaleImage(Image.open(f'{cardNum}.jpg'), 0.5)

def ifGameOver(vegMkt):
    # determine if the game is over
    for vegNum in range(6):
        if vegMkt.cards[vegNum] != None:
            return False
    return True

def heuristic(player1, player2):
    player1Score = player1.getScore()
    player2Score = player2.getScore()
    return player1Score - player2Score

def minimax(piles, vegMkt, player1, player2, depth, playerNum):
    if depth == 0 or ifGameOver(vegMkt):
        return heuristic(player1, player2)
    if playerNum == 1:
        maxEval = -math.inf
        # for all child of current position
            # eval = minimax(piles...for child, depth-1, 2)
            # maxEval = max(maxEval, eval)
        for pileNum in range(3):
            Tpiles = copy.deepcopy(piles)
            TvegMkt = copy.deepcopy(vegMkt)
            Tplayer1 = copy.deepcopy(player1)
            Tplayer2 = copy.deepcopy(player2)
            Tplayer1.drawFromPile(Tpiles[pileNum])
            evl = minimax(Tpiles, TvegMkt, Tplayer1, Tplayer2, depth-1, 2)
            maxEval = max(maxEval, evl)
        for i in range(6):
            for j in range(6):
                Tpiles = copy.deepcopy(piles)
                TvegMkt = copy.deepcopy(vegMkt)
                Tplayer1 = copy.deepcopy(player1)
                Tplayer2 = copy.deepcopy(player2)
                Tplayer1.drawFromVegMkt(vegMkt, i)
                TvegMkt.drawFromPile(Tpiles, i)
                Tplayer1.drawFromVegMkt(TvegMkt, j)
                TvegMkt.drawFromPile(Tpiles, j)
                evl = minimax(Tpiles, TvegMkt, Tplayer1, Tplayer2, depth-1, 2)
                maxEval = max(maxEval, evl)
        return maxEval
    else:
        minEval = math.inf
        # for all child of current position
            # eval = minimax(piles...for child, depth-1, 1)
            # minEval = min(minEval, eval)
        for pileNum in range(3):
            Tpiles = copy.deepcopy(piles)
            TvegMkt = copy.deepcopy(vegMkt)
            Tplayer1 = copy.deepcopy(player1)
            Tplayer2 = copy.deepcopy(player2)
            Tplayer2.drawFromPile(Tpiles[pileNum])
            evl = minimax(Tpiles, TvegMkt, Tplayer1, Tplayer2, depth-1, 1)
            minEval = min(minEval, evl)
        for i in range(6):
            for j in range(6):
                Tpiles = copy.deepcopy(piles)
                TvegMkt = copy.deepcopy(vegMkt)
                Tplayer1 = copy.deepcopy(player1)
                Tplayer2 = copy.deepcopy(player2)
                Tplayer2.drawFromVegMkt(TvegMkt, i)
                TvegMkt.drawFromPile(Tpiles, i)
                Tplayer2.drawFromVegMkt(TvegMkt, j)
                TvegMkt.drawFromPile(Tpiles, j)
                evl = minimax(Tpiles, TvegMkt, Tplayer1, Tplayer2, depth-1, 1)
                minEval = min(minEval, evl)
        return minEval

def arePilesEmpty(app):
    # determine if the draw piles are empty
    for pileNum in app.piles:
        if app.piles[pileNum] != None:
            return False
    return True

def vegClicked(app, event):
    # return the veggie number the player clicked
    cx1 = app.width / 8
    cx2 = app.width / 4
    cx3 = app.width * 3/8
    cy1 = app.height / 2
    cy2 = app.height * 3/4
    width = app.cardWidth
    height = app.cardHeight
    if (cx1-width/2 <= event.x <= cx1+width/2 and
        cy1-height/2 <= event.y <= cy1+height/2):
        return 0
    elif (cx1-width/2 <= event.x <= cx1+width/2 and
        cy2-height/2 <= event.y <= cy2+height/2):
        return 1
    elif (cx2-width/2 <= event.x <= cx2+width/2 and
        cy1-height/2 <= event.y <= cy1+height/2):
        return 2
    elif (cx2-width/2 <= event.x <= cx2+width/2 and
        cy2-height/2 <= event.y <= cy2+height/2):
        return 3
    elif (cx3-width/2 <= event.x <= cx3+width/2 and
        cy1-height/2 <= event.y <= cy1+height/2):
        return 4
    elif (cx3-width/2 <= event.x <= cx3+width/2 and
        cy2-height/2 <= event.y <= cy2+height/2):
        return 5
    else:
        return None

def pileClicked(app, event):
    # return the pile number the player clicked
    cx1 = app.width / 8
    cx2 = app.width / 4
    cx3 = app.width * 3/8
    cy = app.height / 4
    width = app.cardWidth
    height = app.cardHeight
    if cy-height/2 <= event.y <= cy+height/2:
        if cx1-width/2 <= event.x <= cx1+width/2:
            return 0
        if cx2-width/2 <= event.x <= cx2+width/2:
            return 1
        if cx3-width/2 <= event.x <= cx3+width/2:
            return 2
    else:
        return None

def restartButtonClicked(app, event):
    x0 = 10
    y0 = 10
    x1 = 140
    y1 = 50
    # check if restart button is clicked
    return x0 <= event.x <= x1 and y0 <= event.y <= y1

def mousePressed(app, event):
    if app.gameOver == False and app.isStarted == True:
        if restartButtonClicked(app, event):
            appStarted(app)
        vegNum = vegClicked(app, event)
        pileNum = pileClicked(app, event)
        if vegNum != None and app.vegMkt.cards[vegNum] != None:
            # check if the clicked card is empty
            if app.counter % 2 == 0:
                app.isVegClickedPrev = not app.isVegClickedPrev
                # account for 2 veggies in a row
                app.player1.drawFromVegMkt(app.vegMkt, vegNum)
                app.vegMkt.drawFromPile(app.piles, vegNum)
                if app.isVegClickedPrev:
                # account for 2 veggies in a row
                    app.counter += 2
                else:
                    app.counter += 1
            elif (not app.inBotMode and 
            not app.inNormalBotMode and 
            not app.inHardBotMode and
            not app.inDynamicBotMode):
                app.isVegClickedPrev = not app.isVegClickedPrev
                # account for 2 veggies in a row
                app.player2.drawFromVegMkt(app.vegMkt, vegNum)
                app.vegMkt.drawFromPile(app.piles, vegNum)
                if app.isVegClickedPrev:
                # account for 2 veggies in a row
                    app.counter += 2
                else:
                    app.counter += 1
            if ifGameOver(app.vegMkt):
                # check if the game is over after drafting
                app.gameOver = True       
        elif (pileNum != None and app.piles[pileNum] != None and
            app.isVegClickedPrev == False):
            # check if the clicked pile is empty 
            # and account for 2 veggies in a row
            if app.counter % 2 == 0:
                app.player1.drawFromPile(app.piles[pileNum])
                app.counter += 1
            elif (not app.inBotMode and 
            not app.inNormalBotMode and 
            not app.inHardBotMode and
            not app.inDynamicBotMode):
                app.player2.drawFromPile(app.piles[pileNum])
                app.counter += 1
        elif app.counter % 2 == 0:
            app.player1.optionalFlip(app, event) 
            # this fn updates the counter when a card is flipped
        elif (not app.inBotMode and
        not app.inNormalBotMode and
        not app.inHardBotMode and
        not app.inDynamicBotMode):
            app.player2.optionalFlip(app, event)

def keyPressed(app, event):
    if event.key == 'e':
    # press e to play with bot
        if app.inBotMode == False and app.isStarted == False:
            app.inBotMode = True
            app.isStarted = True
            app.player2 = BotPlayer(2)
    if event.key == 'n':
    # press n to play with normal bot
        if app.inNormalBotMode == False and app.isStarted == False:
            app.inNormalBotMode = True
            app.isStarted = True
            app.player2 = BotPlayer(2)
    if event.key == 'h':
    # press h to play with hard bot
        if app.inHardBotMode == False and app.isStarted == False:
            app.inHardBotMode = True
            app.isStarted = True
            app.player2 = BotPlayer(2)
    if event.key == 'd':
    # press d to play with dynamic difficulty
        if app.inDynamicBotMode == False and app.isStarted == False:
            app.inDynamicBotMode = True
            app.isStarted = True
            app.player2 = BotPlayer(2)
    if event.key == 's':
    # press s to start
        if app.isStarted == False:
            app.isStarted = True
    if event.key == 'r':
    # press r to restart
        if app.gameOver == True:
            appStarted(app)

def timerFired(app):
    if app.isStarted and not app.gameOver:
        if app.inBotMode:
            # let the bot handle its movements if in bot mode
            app.player2.autoPilot(app)
        if app.inNormalBotMode:
            app.player2.normalAutoPilot(app)
        if app.inHardBotMode:
            app.player2.hardAutoPilot(app)
        if app.inDynamicBotMode:
            app.player2.dynamicAutoPilot(app)
    
def drawPilesArea(app, canvas):
    # draw the draw piles area
    x0 = 0
    y0 = 0
    x1 = app.width / 2
    y1 = app.height * 3/8
    canvas.create_rectangle(x0, y0, x1, y1, fill='')
    canvas.create_text(x0+5, y1-5, anchor=SW, text='Draw \nPiles',
    font='Arial 18')

def drawRestartButton(app, canvas):
    # draw the restart button
    x0 = 10
    y0 = 10
    x1 = 140
    y1 = 50
    cx = (x0+x1) / 2
    cy = (y0+y1) / 2
    canvas.create_rectangle(x0, y0, x1, y1, fill='')
    canvas.create_text(cx, cy, text='RESTART', font='Arial 18')

def drawInstructions(app, canvas):
    # draw the instructions during play
    cx = app.width / 4
    cy = app.height / 8
    text = 'Click on a card to draw. You can draw 2 veggie cards from\n'\
        'the veggie market or 1 point card from the draw piles per turn.'
    canvas.create_text(cx, cy, anchor=S, text=text, font='Arial 14')

def drawPlayer1Score(app, canvas, score):
    # draw player1's score
    cx = app.width / 4
    cy = app.height * 3/4
    canvas.create_text(cx, cy, text=f'Player 1 Score: {score}', font='Arial 18')

def drawPlayer2Score(app, canvas, score):
    # draw player2's score
    cx = app.width * 3/4
    cy = app.height * 3/4
    canvas.create_text(cx, cy, text=f'Player 2 Score: {score}', font='Arial 18')

def drawPlayer1Win(app, canvas):
    # draw win screen for player1
    cx = app.width / 2
    cy = app.height / 2
    canvas.create_text(cx, cy, text='Player 1 has won', font='Arial 40 bold')

def drawPlayer2Win(app, canvas):
    # draw win screen for player2
    cx = app.width / 2
    cy = app.height / 2
    canvas.create_text(cx, cy, text='Player 2 has won', font='Arial 40 bold')

def drawDrawScreen(app, canvas):
    # draw draw screen
    cx = app.width / 2
    cy = app.height / 2
    canvas.create_text(cx, cy, text='The game ended with a draw', 
                       font='Arial 40 bold')

def drawRestartDirections(app, canvas):
    # draw restart directions
    cx = app.width / 2 
    cy = app.height / 2 + 50
    canvas.create_text(cx, cy, text='Press R to restart',
                       font='Arial 18')

def drawStartScreen(app, canvas):
    # draw the start screen
    cx = app.width / 2
    cy = app.height / 2
    title = 'POINT SALAD'
    start = 'Press S to start a 2-player game\n'\
        'Press E to play with an easy bot\nPress N to play with a normal bot\n'\
        'Press H to play with a hard bot\nPress D for dynamic difficulty'
    overview = 'Welcome! \n'\
        'Point Salad is a card-drafting and tableau-building game. \n'\
        'Players take turns building a salad of veggies and collecting\n'\
        'point cards in order to score the most points for the \n'\
        'ingredients in their salad!'
    canvas.create_text(cx, cy-150, text=title, font='Arial 64 bold')
    canvas.create_text(cx, cy-50, text=start, font='Arial 18')
    canvas.create_text(cx, cy+150, text=overview, font='Arial 32')

def redrawAll(app, canvas):
    if app.isStarted == False:
        drawStartScreen(app, canvas)
    elif app.gameOver == False:
        drawRestartButton(app, canvas)
        drawInstructions(app, canvas)
        for pileNum in app.piles:
            app.piles[pileNum].drawOnCanvas(app, canvas)
        drawPilesArea(app, canvas)
        app.vegMkt.drawCardsOnCanvas(app, canvas)
        app.vegMkt.drawVegMktArea(app, canvas)
        app.player1.drawPlayerArea(app, canvas)
        app.player2.drawPlayerArea(app, canvas)
        app.player1.drawHighLight(app, canvas)
        app.player2.drawHighLight(app, canvas)
        app.player1.drawCardsOnCanvas(app, canvas)
        app.player2.drawCardsOnCanvas(app, canvas)
    else:
        player1Score = app.player1.getScore()
        player2Score = app.player2.getScore()
        drawPlayer1Score(app, canvas, player1Score)
        drawPlayer2Score(app, canvas, player2Score)
        drawRestartDirections(app, canvas)
        if player1Score > player2Score:
            drawPlayer1Win(app, canvas)
        elif player1Score < player2Score:
            drawPlayer2Win(app, canvas)
        else:
            drawDrawScreen(app, canvas)

runApp(width=1920, height=1080)
