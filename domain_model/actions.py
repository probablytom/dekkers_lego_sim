from forms import B, E
from workflow_graphs import default_cost
from copy import copy


# There's gotta be an easier way.
def send_message(other_actor, message):
    @default_cost(1)
    def _send_message(ctx, actor, env):
        other_actor.recieve_message(message)
    return _send_message

# Sales Department actions
# NOTE: invoked when Sales is passed a Form A (customer order).
def fill_product_code_box(ctx, actor, env):
    ctx["forms"]["B"] = B()
    ctx["forms"]["B"].product_code = ctx["incoming message"].product_code

    # Begin populating the E form with its time recieved
    # (but nothing else until we actually fill the form in, this is its own action)
    ctx["forms"]["E entry"] = E.Entry()
    ctx["forms"]["E entry"].time_recieved = actor["self"].clock.ticks_passed

def set_scheduled_lead_time(ctx, actor, env):  #What's the scheduled lead time?
    # TODO HAVE TO MAKE A DECISION HERE ABOUT HOW LONG WE WANT TO TAKE TO DELIVER THE CAR.
    ctx["forms"]["B"].scheduled_lead_time = env["forms"]["D"]

def fill_out_sales_history_E(ctx, actor, env):
    ctx["forms"]["E entry"].order_number = copy(env["order_counter"])
    env["order_counter"] += 1

    ctx["forms"]["E entry"].product_code = ctx["forms"]["B"].product_code
    ctx["forms"]["E entry"].scheduled_lead_time = ctx["forms"]["B"].scheduled_lead_time

    actor["E"].add_entry(ctx["forms"]["E entry"])

def pass_form_B_to_prod_planning(ctx, actor, env):
    send_message(env["departments"]["production planning"], ctx["forms"]["B"])

def pass_customer_order_to_QA(ctx, actor, env):
    # The incoming message for this workflow is the relevant Form A.
    send_message(env["departments"]["qa"], ctx["incoming message"])

# Production planning actions
def find_product_code_from_order_form_B(ctx, actor, env):
    ctx["forms"]["B"] = copy(ctx["incoming message"])  # Product code is on form

def identify_correct_Bill_of_Materials_F(ctx, actor, env):
    ctx["forms"]["F"] = F(ctx["forms"]["B"].product_code)

def fill_out_picklist_M(ctx, actor, env):
    raise NotImplemented()

def pass_M_to_Supplier(ctx, actor, env):
    send_message(env["departments"]["supplier"], ctx["forms"]["M"])

def pass_order_form_to_shop_floor_control(ctx, actor, env):
    raise NotImplemented()

# Supplier actions
def identify_materials_according_to_picklist(ctx, actor, env):
    raise NotImplemented()

def collect_materials(ctx, actor, env):
    raise NotImplemented()

def put_materials_in_box(ctx, actor, env):
    raise NotImplemented()

def put_picklist_in_box(ctx, actor, env):
    raise NotImplemented()

def pass_box_to_goods_reciept(ctx, actor, env):
    raise NotImplemented()


# Goods reciept department actions
def correct_materials_received(ctx, actor, env):
    raise NotImplemented()

def return_box_and_picklist_to_supplier(ctx, actor, env):
    raise NotImplemented()

def fill_out_order_section_of_goods_history(ctx, actor, env):
    raise NotImplemented()

def fill_out_product_section_of_goods_history(ctx, actor, env):
    raise NotImplemented()

def pass_box_and_picklist_to_shop_floow_control(ctx, actor, env):
    raise NotImplemented()


# Shop floor control department actions
def select_production_instructions(ctx, actor, env):
    raise NotImplemented()

def pass_box_to_production_department(ctx, actor, env):
    raise NotImplemented()

def wait_for_production_capacity(ctx, actor, env):
    raise NotImplemented()

def pass_box_to_production_department(ctx, actor, env):
    raise NotImplemented()


# Production department actions
def produce_car(ctx, actor, env):
    raise NotImplemented()

def pass_car_and_forms_to_qa(ctx, actor, env):
    raise NotImplemented()

def return_box_to_supplier(ctx, actor, env):
    raise NotImplemented()

def return_instructions_to_shop_floor_control(ctx, actor, env):
    raise NotImplemented()


# QA acitons
def store_order_form(ctx, actor, env):
    raise NotImplemented()

def match_car_to_customer_order(ctx, actor, env):
    raise NotImplemented()

def car_produced_matches_order(ctx, actor, env):
    raise NotImplemented()

def sign_order_form(ctx, actor, env):
    raise NotImplemented()

def send_car_and_picklist_and_orderform_to_manager(ctx, actor, env):
    raise NotImplemented()

def fill_out_qa_form(ctx, actor, env):
    raise NotImplemented()

def send_forms_and_car_to_manager(ctx, actor, env):
    raise NotImplemented()


# Financial admin kit price
def fill_out_kit_price(ctx, actor, env):
    raise NotImplemented()

def wait_for_ayn_employee_history_from_manager(ctx, actor, env):
    raise NotImplemented()

def complete_profit_and_loss(ctx, actor, env):
    raise NotImplemented()


# Manager actions
def record_employees(ctx, actor, env):
    raise NotImplemented()

def pass_AYN_history_and_order_forms_to_fin_admin(ctx, actor, env):
    raise NotImplemented()

def car_made_correctly(ctx, actor, env):
    raise NotImplemented()

def send_car_to_relevant_department(ctx, actor, env):
    raise NotImplemented()

def deliver_car_to_customer(ctx, actor, env):
    raise NotImplemented()

def fill_out_order_form(ctx, actor, env):
    raise NotImplemented()

def update_cars_delivered(ctx, actor, env):
    raise NotImplemented()

