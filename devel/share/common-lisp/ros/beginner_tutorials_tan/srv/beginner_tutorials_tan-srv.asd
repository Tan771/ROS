
(cl:in-package :asdf)

(defsystem "beginner_tutorials_tan-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoInt" :depends-on ("_package_AddTwoInt"))
    (:file "_package_AddTwoInt" :depends-on ("_package"))
  ))