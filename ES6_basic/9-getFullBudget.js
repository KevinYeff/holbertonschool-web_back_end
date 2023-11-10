import getBudgetObject from './7-getBudgetObject';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    // This is just for good practices, you can use brakets and the return keyword.
    getIncomeInDollars: (income) => `$${income}`,
    // Or not.
    getIncomeInEuros: (income) => `${income} euros`,
  };

  return fullBudget;
}
