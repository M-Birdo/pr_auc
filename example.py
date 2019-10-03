#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# prepare data
sample_data = pd.read_csv('test.csv')
y_test = sample_data.y_test
y_proba = sample_data.y_proba


#get the points in ROC and PR space
Points_ROC = points(y_test, y_proba, space = 'ROC')
Points_PR  = points(y_test, y_proba, space = 'PR')

# caclulate AUC PR score
auc_pr, INTERPOLATION, CONVEX_HULL = auc_pr_score(y_test, Points_ROC, Points_PR)

print('AUC PR score: %.2f'%auc_pr)

# plot PR curve 
plot_auc_pr(auc_pr, Points_PR)

