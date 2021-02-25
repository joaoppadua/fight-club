#Script to calculate probatilities


class Prob:
    def __init__(self, target, population):
        self.target = target
        self.pop = population
    
    def freq(self):
        return self.target/self.pop

    def bayesian(self, condition, likelihood):
        prior = self.freq()
        bayes_prob = likelihood*prior/condition
        return bayes_prob


#Applied to Brazilian prison population
populacao_carceraria = 748009 # https://app.powerbi.com/view?r=eyJrIjoiZWI2MmJmMzYtODA2MC00YmZiLWI4M2ItNDU2ZmIyZjFjZGQ0IiwidCI6ImViMDkwNDIwLTQ0NGMtNDNmNy05MWYyLTRiOGRhNmJmZThlMSJ9
populacao_brasileira = 212.750*10**6 # https://www.ibge.gov.br/apps/populacao/projecao/index.html
presos_curso_superior = 0.005 # https://www.conjur.com.br/2020-set-15/tribuna-defensoria-mito-justica-penal-igualitaria-brasil#_ftn2
populacao_curso_superior = 1/3

prisao = Prob(populacao_carceraria, populacao_brasileira)
prob_prisao = prisao.freq()
prob_prisao_cond_superior = prisao.bayesian(populacao_curso_superior, presos_curso_superior)

print(f'\nProbabilidade de alguem ser preso no Brasil: {prob_prisao}')
print(f'\nProbabilidade bayesiana de alguem com curso superior ser preso no Brasil: {prob_prisao_cond_superior}')
print(f'\nOdds-ratio: {prob_prisao/prob_prisao_cond_superior}')
