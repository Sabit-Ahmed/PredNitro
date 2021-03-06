import matplotlib.pyplot as plt
import os
from sklearn.metrics import roc_curve, auc
import pandas as pd

absolute_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..\\..\\..\\..\\'))
training_result_path = absolute_path + '\\training\\PredNTS Dataset\\result\\'
test_result_path = absolute_path +"\\test\\result\\"

y_train_label = pd.read_csv(training_result_path + "SVM\\y_test_5fold.csv", index_col=[0])
y_train_predicted_label = pd.read_csv(training_result_path + "SVM\\y_pred_5fold.csv", index_col=[0])

y_test_label = pd.read_csv(test_result_path + "y_test.csv", index_col=[0])
y_test_predicted_label = pd.read_csv(test_result_path + "y_pred_score.csv", index_col=[0])

fpr2, tpr2, _2 = roc_curve(y_true=y_train_label, y_score=y_train_predicted_label, pos_label=1)
fpr3, tpr3, _3 = roc_curve(y_true=y_test_label, y_score=y_test_predicted_label, pos_label=1)

roc_auc2 = auc(fpr2, tpr2)
roc_auc3 = auc(fpr3, tpr3)


plt.figure()
plt.plot(fpr2,tpr2, color="navy",lw=4, linestyle=":", label="5-fold cross-validation (AUC = %0.4f)" % roc_auc2)
plt.plot(fpr3,tpr3, color="red",lw=4, linestyle="-", label="Independent test (AUC = %0.4f)" % roc_auc3)
plt.plot([0,1], [0,1], color="gray",lw=1.5, linestyle="-.")

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel("1 - Specificity")
plt.ylabel("Sensitivity")
plt.title("ROC curve of PredNitro")
plt.legend(loc="lower right")
# plt.show()
plt.savefig(fname=training_result_path + "\\ROC_Curve\\ROC_PredNitro.png")