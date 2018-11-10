from workflow_graphs import *

# Set up the graphs
sales_dept_workflow = WorkflowGraph()
production_planning_workflow = WorkflowGraph()
supplier = WorkflowGraph()
goods_receipt = WorkflowGraph()
shop_floor_control = WorkflowGraph()
production_dept = WorkflowGraph()
qa_receiving_customer_order = WorkflowGraph()
qa_receiving_produced_car = WorkflowGraph()
financial_admin_dept = WorkflowGraph()
manager_game_starts = WorkflowGraph()
manager_game_ends = WorkflowGraph()
manager_receives_car = WorkflowGraph()


# I'm inventing an undocumented "game marshal" who dictates things like when the game begins and ends.


# =====
# sales department workflow
# =====

# The sales department workflow is instigated with a message from the customer, held in the Context.
# Relevant context keys are: TODO

# TODO: have sub-workflows properly accepted. Requires re-engineering internal representation to e.g. adjacency lists.
fill_in_order_form_B = WorkflowGraph()
fill_in_order_form_B\
    .begin_with(fill_product_code_box)\
    .then(set_scheduled_lead_time)
    # Then end. By default subworkflows should join to whatever larger workflow they're a part of. .then(End) would kill the workflow.

sales_dept_workflow\
    .begin_with(fill_in_order_form_B)\
    .then(fill_out_sales_history_E)\
    .then(pass_form_B_to_prod_planning)\
    .then(pass_customer_order_to_QA)\
    .then(End)


# =====
# production planning workflow
# =====

# The production planning workflow is instigated with a message from the sales dept, held in the context.
# Relevant context keys are: TODO

production_planning_workflow\
    .begin_with(find_product_code_from_order_form_B)\
    .then(identify_correct_Bill_of_Materials_F)\
    .then(fill_out_picklist_M)\
    .then(pass_M_to_Supplier)\
    .then(pass_order_foorm_to_shop_floor_control)\
    .then(End)


# =====
# supplier workflow
# =====

# The supplier workflow receives a picklist from the production planning department.
# relevant context keys are: TODO

supplier\
    .begin_with(identify_materials_according_to_picklist)\
    .then(collect_materials)\
    .then(put_materials_in_box)\
    .then(put_picklist_in_box)\
    .then(pass_box_to_goods_reciept)\
    .then(End)


# =====
# goods receipt workflow
# =====

# The goods receipt workflow receives a box with materials and forms from the production planning department.
# relevant context keys are: TODO

goods_receipt\
    .begin_with(do_nothing)\  # For now. Currently we can't *begin* with a decision - it's a technical limitation I'm working on.
    .decide_on(correct_materials_received)\
    .when(False)\
    .then(return_box_and_picklist_to_supplier)\
    .when(anything_else)\
    .then(fill_out_order_section_of_goods_history)\
    .then(fill_out_product_section_of_goods_history)\
    .then(pass_box_and_picklist_to_shop_floow_control)\
    .join()\
    .then(End)


# =====
# shop floor control workflow
# =====

# The shop floor control workflow receives a box with materials and forms from the production planning department.
# relevant context keys are: TODO

shop_floor_control\
    .begin_with(select_production_instructions)\
    .then(pass_box_to_production_department)\
    .then(wait_for_production_capacity)\
    .then(pass_box_to_production_department)\
    .then(End)

# =====
# production department workflow
# =====

# The production department workflow receives a box with materials and forms from the production planning department.
# relevant context keys are: TODO

production_dept\
    .begin_with(produce_car)\
    .then(pass_car_and_forms_to_qa)\
    .then(return_box_to_supplier)\
    .then(return_instructions_to_shop_floor_control)\
    .then(End)


# =====
# quality assurance department workflow
# =====

# The qa department has two workflows.
#   qa_receiving_customer_order receives a customer order from a sales department.
#     relevant context keys are: TODO
#   qa_receiving_produced_car receives a car, order form and picklist from production.
#     relevant context keys are: TODO

qa_receiving_customer_order\
    .begin_with(store_order_form)\
    .then(End)

qa_receiving_produced_car\
    .begin_with(match_car_to_customer_order)\
    .decide_on(car_produced_matches_order)\
    .when(True)\
    .then(sign_order_form)\
    .then(send_car_and_picklist_and_orderform_to_manager)\
    .when(False)\
    .then(fill_out_qa_form)\
    .then(send_forms_and_car_to_manager)
    .join()\
    .then(End)

# =====
# financial admin department
# =====

# The financial admin department receives a goods history from goods receipt.
# They immediately wait for an AYN employee history from the manager, passed at the end of the game.
# I have a suspicion that this will become two workflows, with the financial admin waiting for a game_over signal from the game marshal.
# relevant context keys are: TODO

financial_admin_dept\
    .begin_with(fill_out_kit_price)
    .then(wait_for_ayn_employee_history_from_manager)\
    .then(complete_profit_and_loss)\
    .then(End)

# =====
# manager
# =====

# The manager has a few workflows that are run in response to different game states.

# Response to a game_start signal. No context keys.
manager_game_starts\
    .begin_with(record_employees)\
    .then(End)

# Response to a game_end signal. No context keys.
manager_game_ends\
    .begin_with(pass_AYN_history_and_order_forms_to_fin_admin)\
    .then(End)

# Response to being sent a car in-game.
# Relevant context keys are: TODO
# TODO: What on earth am I supposed to do with "send car to relevant department"??!?!?!??!!?!??!?!?!?
manager_receives_car\
    .begin_with(do_nothing)\
    .decide_on(car_made_correctly) \
    .when(False).then(send_car_to_relevant_department)\
    .when(True)\
    .then(deliver_car_to_customer)\
    .then(fill_out_order_form)\
    .then(update_cars_delivered)\
    .join()\
    .then(End)

# =====
# game marshal
# =====

# Sends signals like game_end and game_stop
# To be filled in as I need it for modelling. Undocumented by Rob & Marianna.

